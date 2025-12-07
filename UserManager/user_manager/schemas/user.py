from pydantic import BaseModel
from pydantic import ConfigDict


class LoginUserSchema(BaseModel):
    email: str
    password: str


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    first_name: str | None
    last_name: str | None
    tenant_id: int


class CreateUserSchema(LoginUserSchema):
    first_name: str | None = None
    last_name: str | None = None
