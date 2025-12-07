from fastapi import APIRouter
from fastapi import Depends

from user_manager.api.dependencies.auth import get_current_user
from user_manager.api.dependencies.services import get_balance_service
from user_manager.api.dependencies.services import get_jwt_service
from user_manager.api.dependencies.services import get_retell_service
from user_manager.api.dependencies.services import get_user_service
from user_manager.models import User
from user_manager.schemas.jwt import JwtResponseSchema
from user_manager.schemas.user import CreateUserSchema
from user_manager.schemas.user import LoginUserSchema
from user_manager.schemas.user import UserSchema
from user_manager.services.balance import BalanceService
from user_manager.services.jwt import JwtService
from user_manager.services.retell import RetellService
from user_manager.services.user import UserService
from user_manager.settings.logging_route import LoggingRoute

router = APIRouter(route_class=LoggingRoute)


@router.get(
    '/me',
    summary='Get me info',
    response_model=UserSchema,
)
async def get_me(user: User = Depends(get_current_user)) -> User:
    return user


@router.post(
    '/register',
    summary='Register user',
    response_model=JwtResponseSchema,
)
async def register(
    request_data: CreateUserSchema,
    user_service: UserService = Depends(get_user_service),
    jwt_service: JwtService = Depends(get_jwt_service),
    retell_service: RetellService = Depends(get_retell_service),
    balance_service: BalanceService = Depends(get_balance_service),
) -> JwtResponseSchema:
    await user_service.check_registered_user(request_data)
    tenant = await retell_service.create_agent(request_data)
    user = await user_service.create_user(request_data, tenant.id)
    await balance_service.create_balance(tenant.id)
    token = jwt_service.create_jwt_token(user.id)
    return JwtResponseSchema(token=token)


@router.post(
    '/login',
    summary='Register user',
    response_model=JwtResponseSchema,
)
async def login(
    request_data: LoginUserSchema,
    user_service: UserService = Depends(get_user_service),
    jwt_service: JwtService = Depends(get_jwt_service),
) -> JwtResponseSchema:
    user = await user_service.login(request_data)
    token = jwt_service.create_jwt_token(user.id)
    return JwtResponseSchema(token=token)
