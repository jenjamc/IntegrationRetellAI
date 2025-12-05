from datetime import datetime
from datetime import timedelta

from pydantic import BaseModel
from pydantic import computed_field


class UpdateAccreditationSchema(BaseModel):
    user_id: int
    applicant_id: str

    @computed_field  # type: ignore
    @property
    def valid_to(self) -> str:
        return str(datetime.now() + timedelta(days=365))
