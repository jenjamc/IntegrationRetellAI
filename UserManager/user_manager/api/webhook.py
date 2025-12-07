import json

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import Depends

from user_manager import settings
from user_manager.api.dependencies.auth import get_current_user
from user_manager.api.dependencies.services import get_balance_service
from user_manager.api.dependencies.services import get_call_service
from user_manager.api.dependencies.services import get_jwt_service
from user_manager.api.dependencies.services import get_retell_service
from user_manager.api.dependencies.services import get_user_service
from user_manager.api.dependencies.services import get_webhook_service
from user_manager.exceptions import AuthError
from user_manager.models import User
from user_manager.schemas.base import OKSchema
from user_manager.schemas.call import UpdateCallSchema
from user_manager.schemas.jwt import JwtResponseSchema
from user_manager.schemas.user import CreateUserSchema
from user_manager.schemas.user import LoginUserSchema
from user_manager.schemas.user import UserSchema
from user_manager.services.balance import BalanceService
from user_manager.services.call import CallService
from user_manager.services.jwt import JwtService
from user_manager.services.retell import RetellService
from user_manager.services.user import UserService
from user_manager.services.webhook import WebhookService
from user_manager.settings.constants import WebhookEvents
from user_manager.settings.logging_route import LoggingRoute

router = APIRouter(route_class=LoggingRoute)



@router.post(
    '/webhook',
    summary='Webhook from agent',
    response_model=OKSchema,
)
async def handle_webhook(
        request: Request,
        retell_service: RetellService = Depends(get_retell_service),
        call_service: CallService = Depends(get_call_service),
        balance_service: BalanceService = Depends(get_balance_service),
        webhook_service: WebhookService = Depends(get_webhook_service),
):
    try:
        post_data = await request.json()
        valid_signature = webhook_service.verify_webhook(post_data, str(request.headers.get('X-Retell-Signature')))
        if not valid_signature:
            return AuthError('Unauthorized')

        match (post_data['event']):
            case WebhookEvents.CALL_STARTED:
                tenant = await retell_service.get_tenant_by_agent_id(post_data['call']['agent_id'])
                await call_service.set_call_in_progress(post_data['call']['call_id'], tenant.id)
                return OKSchema()

            case WebhookEvents.CALL_ENDED:
                tenant = await retell_service.get_tenant_by_agent_id(post_data['call']['agent_id'])
                update_data = UpdateCallSchema(
                    call_ended_ms=post_data['call']['end_timestamp'],
                    duration_ms=post_data['call']['duration_ms'],
                )
                await call_service.end_call(post_data['call']['call_id'], tenant.id, update_data)
                await balance_service.decrease_balance(tenant.id, update_data.cost_dollars)
                return OKSchema()

            case _:
                return OKSchema()

    except Exception as err:
        print(f'Error in webhook: {err}')
        return HTTPException(status_code=500, detail='Internal Server Error')
