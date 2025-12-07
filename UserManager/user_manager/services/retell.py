import json
from datetime import datetime
from datetime import timedelta
from typing import Sequence

import jwt
from retell import AsyncRetell
from retell.types import AgentResponse
from sqlalchemy import Column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from user_manager import settings
from user_manager.exceptions import DoesNotExistError
from user_manager.models.tenant import Tenant
from user_manager.schemas.retell import AccessTokenSchema
from user_manager.schemas.retell import AgentSchema
from user_manager.schemas.user import CreateUserSchema
from user_manager.services.base import BaseService
from user_manager.settings.constants import ErrorMessages


class RetellService(BaseService[Tenant]):
    MODEL = Tenant

    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.client = AsyncRetell(
            api_key=settings.RETELL_API_KEY,
            timeout=20.0,
        )

    async def create_agent(self, request_data: CreateUserSchema) -> Tenant:
        agent_response = await self.client.agent.create(
            agent_name=f'{request_data.first_name} {request_data.last_name} bot',
            response_engine={
                'llm_id': 'llm_91785ca1994a122efbf0768c86ce',
                'type': 'retell-llm',
            },
            voice_id='11labs-Adrian',
            webhook_url=f'{settings.RETELL_WEBHOOK}/users/webhook',
        )
        agent_schema = AgentSchema(**agent_response.__dict__)
        tenant = await self._create_tenant(agent_schema)
        return tenant


    async def create_web_call(self, agent_id: str) -> AccessTokenSchema:
        agent_response = await self.client.call.create_web_call(
            agent_id=agent_id
        )
        return AccessTokenSchema(call_id=agent_response.call_id, access_token=agent_response.access_token)


    async def get_tenant_by_agent_id(self, agent_id: str) -> Tenant:
        if tenant := await self.fetch_one(filters=(self.MODEL.agent_id == agent_id,)):
            return tenant
        raise DoesNotExistError(ErrorMessages.TENANT_DOES_NOT_EXIST)


    async def get_tenant_by_tenant_id_summary(self, tenant_id: int) -> Tenant:
        options = (
            selectinload(self.MODEL.calls),
            selectinload(self.MODEL.balance),
        )
        return await self.get_tenant_by_tenant_id(tenant_id, options)


    async def get_tenant_by_tenant_id(self, tenant_id: int, options: Sequence = ()) -> Tenant:
        if tenant := await self.fetch_one(filters=(self.MODEL.id == tenant_id,), options=options):
            return tenant
        raise DoesNotExistError(ErrorMessages.TENANT_DOES_NOT_EXIST)

    async def _create_tenant(self, agent_schema: AgentSchema) -> Tenant:
        obj = Tenant(**agent_schema.model_dump())
        return await self.insert_obj(obj)
