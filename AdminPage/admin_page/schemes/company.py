from pydantic import BaseModel


class CompanySchema(BaseModel):
    user_id: int
