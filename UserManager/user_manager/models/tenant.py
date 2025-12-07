from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from user_manager.models.base import BaseModel

if TYPE_CHECKING:
    from user_manager.models.user import User
    from user_manager.models.balance import Balance
    from user_manager.models.call import Call
    from user_manager.models.balance_adjustment import BalanceAdjustment


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

