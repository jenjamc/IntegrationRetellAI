from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from user_manager.models.base import BaseModel

if TYPE_CHECKING:
    from user_manager.models.tenant import Tenant


class Balance(BaseModel):
    __tablename__ = 'balances'

    current_balance: Mapped[Decimal]
    tenant_id: Mapped[int] = mapped_column(ForeignKey('tenants.id'))

    tenant: Mapped['Tenant'] = relationship('Tenant', back_populates='balance')
