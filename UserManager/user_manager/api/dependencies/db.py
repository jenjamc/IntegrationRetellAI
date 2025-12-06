from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from user_manager.settings.db import async_session


async def get_db_session() -> AsyncGenerator['AsyncSession', None]:
    async with async_session() as session:  # type: ignore
        yield session  # type: ignore
