from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import computed_field

from user_manager.models.call import CallStatus
from user_manager.settings import constants


class CallSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    call_id: str
    tenant_id: int
    status: CallStatus
    started_at: datetime
    ended_at: datetime | None
    billed_seconds: int
    cost_dollars: Decimal


class UpdateCallSchema(BaseModel):
    status: CallStatus = CallStatus.ENDED
    call_ended_ms: int
    duration_ms: int

    @computed_field
    @property
    def billed_seconds(self) -> int:
        return self.duration_ms // 1000

    @computed_field
    @property
    def cost_dollars(self) -> Decimal:
        minutes = Decimal(self.billed_seconds / 60)
        if minutes <= 1:
            return constants.COST_CALL_PER_MINUTE

        return minutes * constants.COST_CALL_PER_MINUTE

    @computed_field
    @property
    def ended_at(self) -> datetime:
        return datetime.fromtimestamp(self.call_ended_ms // 1000)
