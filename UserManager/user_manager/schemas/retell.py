from pydantic import BaseModel
from pydantic import ConfigDict

from user_manager.schemas.balance import BalanceSchema
from user_manager.schemas.call import CallSchema


class AgentSchema(BaseModel):
    agent_name: str
    agent_id: str


class TenantSchema(AgentSchema):
    model_config = ConfigDict(from_attributes=True)

    calls: list[CallSchema]
    balance: BalanceSchema


class AccessTokenSchema(BaseModel):
    call_id: str
    access_token: str
