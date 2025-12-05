from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from admin_page.models.admin_page.base import BaseModel
from admin_page.models.admin_page.roles import permission_roles_relation

if TYPE_CHECKING:
    from admin_page.models.admin_page.roles import AdminRole


class AdminPermission(BaseModel):
    __tablename__ = 'permissions'

    name: Mapped[str]
    description: Mapped[str | None]

    roles: Mapped[list['AdminRole']] = relationship(
        'AdminRole',
        secondary=permission_roles_relation,
        back_populates='permissions',
    )

    def __str__(self):
        return f'{self.name} - ({self.description})'
