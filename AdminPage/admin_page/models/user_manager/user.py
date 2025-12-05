from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from admin_page.exceptions import HTTPClientError
from admin_page.models.user_manager.base import BaseModel






class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    password: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f'{self.id}: {self.email}'