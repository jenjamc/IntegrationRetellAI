from typing import TYPE_CHECKING

import flask_login
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from admin_page.models.admin_page.base import BaseModel

if TYPE_CHECKING:
    from admin_page.models.admin_page.roles import AdminRole


class AdminUser(BaseModel, flask_login.UserMixin):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(unique=True)

    role_id: Mapped[int | None] = mapped_column(ForeignKey('roles.id'))

    role: Mapped['AdminRole'] = relationship('AdminRole', back_populates='users')

    def __str__(self):
        return self.email
