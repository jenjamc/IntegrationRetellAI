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
    ALLOWED_ORIGINS: str = 'http://localhost'

    DB_DRIVER: str = 'postgresql+asyncpg'
    DB_USER: str = 'postgres'
    DB_PASS: str = 'postgres'
    DB_HOST: str = 'db'
    DB_PORT: int = 5432
    DB_NAME: str = 'user_manager'

    SECRET_KEY: str = 'your-secret-key'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    @property
    def sqlalchemy_database_uri(self) -> str:
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'  # noqa


settings = Settings()
