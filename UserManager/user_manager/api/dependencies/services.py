from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user_manager.api.dependencies.db import get_db_session
from user_manager.services.balance import BalanceService
from user_manager.services.call import CallService
from user_manager.services.jwt import JwtService
from user_manager.services.retell import RetellService
from user_manager.services.user import UserService
from user_manager.services.webhook import WebhookService


async def get_user_service(session: AsyncSession = Depends(get_db_session)) -> UserService:
    return UserService(session=session)


async def get_retell_service(session: AsyncSession = Depends(get_db_session)) -> RetellService:
    return RetellService(session=session)


async def get_balance_service(session: AsyncSession = Depends(get_db_session)) -> BalanceService:
    return BalanceService(session=session)


async def get_call_service(session: AsyncSession = Depends(get_db_session)) -> CallService:
    return CallService(session=session)


async def get_jwt_service() -> JwtService:
    return JwtService()


async def get_webhook_service() -> WebhookService:
    return WebhookService()
