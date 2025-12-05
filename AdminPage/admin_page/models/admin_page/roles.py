from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import Table
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from admin_page.models.admin_page.base import Base
from admin_page.models.admin_page.base import BaseModel

if TYPE_CHECKING:
    from admin_page.models.admin_page.permission import AdminPermission

permission_roles_relation = Table(
    'permission_roles_relation',
    Base.metadata,
    sa.Column('role_id', sa.ForeignKey('roles.id'), primary_key=True),
    sa.Column('permission_id', sa.ForeignKey('permissions.id'), primary_key=True),
)


class AdminRole(BaseModel):
    __tablename__ = 'roles'

    name: Mapped[str]

    permissions: Mapped[list['AdminPermission']] = relationship(
        'AdminPermission',
        secondary=permission_roles_relation,
        back_populates='roles',
    )
    users: Mapped[list['AdminRole']] = relationship('AdminUser', back_populates='role')

    def __str__(self):
        return self.name
