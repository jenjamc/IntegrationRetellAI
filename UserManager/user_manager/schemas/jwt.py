from pydantic import BaseModel


class JwtResponseSchema(BaseModel):
    token: str
