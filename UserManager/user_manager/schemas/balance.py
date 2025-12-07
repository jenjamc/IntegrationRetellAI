from decimal import Decimal

from pydantic import BaseModel


class BalanceSchema(BaseModel):
    current_balance: Decimal
