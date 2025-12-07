import json
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Sequence

import jwt
from retell import AsyncRetell
from retell import Retell
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


class WebhookService:

    def __init__(self):
        self.client = Retell(
            api_key=settings.RETELL_WEBHOOK_KEY,
            timeout=20.0,
        )

    def verify_webhook(self, post_data: Any, signature: str) -> bool:
        return self.client.verify(
            json.dumps(post_data, separators=(',', ':'), ensure_ascii=False),
            api_key=settings.RETELL_WEBHOOK_KEY,
            signature=signature,
        )
