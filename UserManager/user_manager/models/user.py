from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from user_manager.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password_hash: Mapped[str] = mapped_column(unique=True)
