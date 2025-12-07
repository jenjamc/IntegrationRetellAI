from user_manager.models.call import Call
from user_manager.models.call import CallStatus
from user_manager.schemas.call import UpdateCallSchema
from user_manager.services.base import BaseService
from user_manager.settings import constants


class CallService(BaseService[Call]):
    MODEL = Call

    async def create_call(self, call_id: str, tenant_id: int) -> Call:
        obj = Call(
            call_id=call_id,
            tenant_id=tenant_id,
            cost_dollars=constants.COST_CALL_PER_MINUTE,
        )
        return await self.insert_obj(obj)

    async def set_call_in_progress(self, call_id: str, tenant_id: int) -> None:
        await self.update(
            filters=(
                self.MODEL.call_id == call_id,
                self.MODEL.tenant_id == tenant_id,
            ),
            values={'status': CallStatus.IN_PROGRESS},
        )

    async def end_call(self, call_id: str, tenant_id: int, update_data: UpdateCallSchema) -> None:
        await self.update(
            filters=(
                self.MODEL.call_id == call_id,
                self.MODEL.tenant_id == tenant_id,
            ),
            values=update_data.model_dump(exclude={'call_ended_ms', 'duration_ms'}),
        )
