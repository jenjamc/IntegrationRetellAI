from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from user_manager.settings.conf import settings


print('settings.sqlalchemy_database_urisettings.sqlalchemy_database_uri', settings.sqlalchemy_database_uri)
engine = create_async_engine(settings.sqlalchemy_database_uri)
async_session = sessionmaker(None, expire_on_commit=False, class_=AsyncSession)
