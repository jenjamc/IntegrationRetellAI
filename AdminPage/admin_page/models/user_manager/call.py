from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from admin_page.models.user_manager import BaseModel

if TYPE_CHECKING:
    from admin_page.models.user_manager.user import Tenant


class CallStatus(StrEnum):
    STARTED = 'started'
    IN_PROGRESS = 'in_progress'
    ENDED = 'ended'


class Call(BaseModel):
    __tablename__ = 'calls'

    call_id: Mapped[str] = mapped_column(unique=True)
    tenant_id : Mapped[int] = mapped_column(ForeignKey('tenants.id'))
    status: Mapped[CallStatus] = mapped_column(default=CallStatus.STARTED)
    started_at: Mapped[datetime] = mapped_column(default=datetime.now)
    ended_at: Mapped[datetime] = mapped_column(nullable=True)
    billed_seconds: Mapped[int] = mapped_column(default=0)
    cost_dollars: Mapped[Decimal] = mapped_column(default=Decimal('0.00'))

    tenant: Mapped['Tenant'] = relationship('Tenant', back_populates='calls')
