from enum import Enum

from pydantic_settings import BaseSettings


class Env(str, Enum):
    TESTING = 'TESTING'
    LOCAL = 'LOCAL'
    DEV = 'DEV'
    STAGING = 'STAGING'
    PRODUCTION = 'PRODUCTION'


class LogLevel(str, Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class Settings(BaseSettings):
    PORT: int = 4000
    ENV: Env = Env.PRODUCTION
    DEBUG: bool = False
    LOG_LEVEL: str = LogLevel.INFO
    ALLOWED_ORIGINS: str = 'http://localhost http://localhost:3000 http://127.0.0.1:3000'
    SECRET_KEY: str = 'secret_key'

    DB_DRIVER: str = 'postgresql'
    DB_USER: str = 'postgres'
    DB_PASS: str = 'postgres'
    DB_HOST: str = 'db'
    DB_PORT: int = 5432

    DB_NAME_ADMIN_PAGE: str = 'admin_page'
    DB_NAME_USER_MANAGER: str = 'user_manager'

    @property
    def database_uri(self) -> str:
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/'  # noqa


settings = Settings()
