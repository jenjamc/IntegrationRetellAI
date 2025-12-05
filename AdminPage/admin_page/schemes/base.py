from pydantic import BaseModel


class OKSchema(BaseModel):
    OK: bool = True
