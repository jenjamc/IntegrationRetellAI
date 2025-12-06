from datetime import datetime
from datetime import timedelta

import jwt
from sqlalchemy import Column

from user_manager import settings


class JwtService:
    @staticmethod
    def create_jwt_token(user_id: Column[int]) -> str:
        expire = datetime.now(tz=None) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token_data = {'sub': str(user_id), 'exp': expire}
        return jwt.encode(token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# agent_78233f717b41c36cb4f5266491