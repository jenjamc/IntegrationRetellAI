import hashlib

import pyotp
from passlib.context import CryptContext
from pydantic import EmailStr
from pydantic import TypeAdapter
from sqlalchemy import desc
from sqlalchemy import distinct
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from user_manager.exceptions import DoesNotExistError
from user_manager.exceptions import ValidationError
from user_manager.models import User
from user_manager.schemas.user import CreateUserSchema
from user_manager.schemas.user import LoginUserSchema
from user_manager.services.base import BaseService
from user_manager.settings.constants import ErrorMessages


class UserService(BaseService[User]):
    MODEL = User

    async def get_user_by_id(self, user_id: int) -> User | None:
        if user := await self.fetch_one(filters=(self.MODEL.id == user_id,)):
            return user
        raise DoesNotExistError(ErrorMessages.USER_DOES_NOT_EXIST)


    async def get_user_by_email(self, email: str) -> User | None:
        if user := await self.fetch_one(filters=(self.MODEL.email == email,)):
            return user
        raise DoesNotExistError(ErrorMessages.USER_DOES_NOT_EXIST)

    async def create_user(self, user: CreateUserSchema) -> User:
        obj = User(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password_hash=self.hash_password(user.password)
        )
        return await self.insert_obj(obj)

    async def login(self, request_data: LoginUserSchema) -> User:
        user = await self.get_user_by_email(request_data.email)

        if not self.verify_password(request_data.password, user.password_hash):
            raise ValidationError(ErrorMessages.INVALID_PASSWORD)

        return user


    def hash_password(self, password: str):
        return self.get_pass_hex(password)

    def verify_password(self, password, password_hash):
        return self.get_pass_hex(password) == password_hash

    @staticmethod
    def get_pass_hex(password: str):
        password_bytes = password.encode('utf-8')
        sha = hashlib.sha256(password_bytes).hexdigest()
        return sha

