from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from admin_page.models.user_manager import BaseModel

if TYPE_CHECKING:
    from admin_page.models.user_manager.user import User
    from admin_page.models.user_manager.balance import Balance
    from admin_page.models.user_manager.call import Call
    from admin_page.models.user_manager.balance_adjustment import BalanceAdjustment


class Tenant(BaseModel):
    __tablename__ = 'tenants'

    agent_name: Mapped[str]
    agent_id: Mapped[str]

    user: Mapped['User'] = relationship('User', back_populates='tenant')
    balance: Mapped['Balance'] = relationship('Balance', back_populates='tenant')
    calls: Mapped[list['Call']] = relationship('Call', back_populates='tenant')
    balance_adjustments: Mapped[list['BalanceAdjustment']] = relationship(
        'BalanceAdjustment',
        back_populates='tenant',
    )

    def __repr__(self):
        return f'{self.agent_name}'

