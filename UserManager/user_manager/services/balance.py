from decimal import Decimal

from user_manager.exceptions import DoesNotExistError
from user_manager.exceptions import ValidationError
from user_manager.models.balance import Balance
from user_manager.services.base import BaseService
from user_manager.settings.constants import ErrorMessages


class BalanceService(BaseService[Balance]):
    MODEL = Balance

    async def create_balance(self, tenant_id: int) -> Balance:
        obj = Balance(
            current_balance=Decimal('200'),
            tenant_id=tenant_id,
        )
        return await self.insert_obj(obj)

    async def verify_balance(self, tenant_id: int) -> None:
        balance = await self._get_balance(tenant_id)
        if balance.current_balance <= 0:
            raise ValidationError(ErrorMessages.INSUFFICIENT_FUNDS)

    async def _get_balance(self, tenant_id: int) -> Balance:
        if balance := await self.fetch_one(filters=(self.MODEL.tenant_id == tenant_id,)):
            return balance
        raise DoesNotExistError(ErrorMessages.BALANCE_DOES_NOT_EXIST)

    async def decrease_balance(self, tenant_id: int, cost: Decimal) -> Balance:
        balance = await self._get_balance(tenant_id)
        left_balance = balance.current_balance - cost
        await self.update_obj(balance, {'current_balance': left_balance})
        return balance
