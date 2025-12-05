from pydantic import BaseModel
from pydantic import Field


class ResponsePassphraseSchema(BaseModel):
    passphrase_id: str = Field(..., alias='passphraseId')
