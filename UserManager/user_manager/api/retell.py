from fastapi import APIRouter
from fastapi import Depends

from user_manager.api.dependencies.auth import get_current_user
from user_manager.api.dependencies.services import get_balance_service
from user_manager.api.dependencies.services import get_call_service
from user_manager.api.dependencies.services import get_jwt_service
from user_manager.api.dependencies.services import get_retell_service
from user_manager.api.dependencies.services import get_user_service
from user_manager.models import Tenant
from user_manager.models import User
from user_manager.schemas.jwt import JwtResponseSchema
from user_manager.schemas.retell import AccessTokenSchema
from user_manager.schemas.retell import TenantSchema
from user_manager.schemas.user import CreateUserSchema
from user_manager.schemas.user import LoginUserSchema
from user_manager.schemas.user import UserSchema
from user_manager.services.balance import BalanceService
from user_manager.services.call import CallService
from user_manager.services.jwt import JwtService
from user_manager.services.retell import RetellService
from user_manager.services.user import UserService
from user_manager.settings.logging_route import LoggingRoute

router = APIRouter(route_class=LoggingRoute, prefix='/tenant')


@router.get(
    '/bot',
    summary='Get Bot Info',
    response_model=TenantSchema,
)
async def get_bot(
        user: User = Depends(get_current_user),
        retell_service: RetellService = Depends(get_retell_service),
) -> Tenant:
    return await retell_service.get_tenant_by_tenant_id_summary(user.tenant_id)


@router.post(
    '/calls',
    summary='Start call',
    response_model=AccessTokenSchema,
)
async def start_call(
        user: User = Depends(get_current_user),
        balance_service: BalanceService = Depends(get_balance_service),
        retell_service: RetellService = Depends(get_retell_service),
        call_service: CallService = Depends(get_call_service),
) -> AccessTokenSchema:
    await balance_service.verify_balance(user.tenant_id)
    tenant = await retell_service.get_tenant_by_tenant_id(user.tenant_id)
    response = await retell_service.create_web_call(tenant.agent_id)
    await call_service.create_call(response.call_id, tenant.id)
    return response

