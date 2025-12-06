from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user_manager.api.dependencies.db import get_db_session

from user_manager.services.jwt import JwtService
from user_manager.services.user import UserService


async def get_user_service(session: AsyncSession = Depends(get_db_session)) -> UserService:
    return UserService(session=session)


async def get_jwt_service() -> JwtService:
    return JwtService()
