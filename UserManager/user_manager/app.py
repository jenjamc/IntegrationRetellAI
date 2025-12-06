from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from user_manager import version
from user_manager.api import base
from user_manager.api import user
from user_manager.exception_handlers import FastAPIExceptionHandlers
from user_manager.middlewares import init_middlewares
from user_manager.models import metadata
from user_manager.settings.conf import Env
from user_manager.settings.conf import Settings
from user_manager.settings.conf import settings
from user_manager.settings.db import async_session

PREFIX: str = '/users'


def init_routes(fast_api_app: 'FastAPI') -> None:
    fast_api_app.include_router(base.router, prefix=PREFIX, tags=['Base'])
    fast_api_app.include_router(user.router, prefix=PREFIX, tags=['User'])


def init_db(app_settings: Settings):
    engine = create_async_engine(app_settings.sqlalchemy_database_uri)
    async_session.configure(bind=engine)
    metadata.bind = engine  # type: ignore



def create_app(app_settings: Settings = settings) -> FastAPI:
    app_settings = app_settings if app_settings is not None else settings
    is_production = app_settings.ENV == Env.PRODUCTION
    fast_api_app = FastAPI(
        title='Stobox4 User manager API',
        debug=app_settings.DEBUG,
        docs_url=None if is_production else f'{PREFIX}/docs',
        redoc_url=None if is_production else f'{PREFIX}/redoc',
        openapi_url=None if is_production else f'{PREFIX}/openapi.json',
        version=version,
    )
    init_middlewares(fast_api_app)
    FastAPIExceptionHandlers(fast_api_app)
    init_db(app_settings)
    init_routes(fast_api_app)
    return fast_api_app
