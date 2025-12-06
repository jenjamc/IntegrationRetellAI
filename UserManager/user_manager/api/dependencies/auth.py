import logging
from http import HTTPStatus
from typing import Any

import jwt
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from user_manager import settings
from user_manager.api.dependencies.services import get_user_service
from user_manager.models import User
from user_manager.services.user import UserService
from user_manager.settings.constants import ErrorMessages

logger = logging.getLogger(__name__)

oauth2_scheme = HTTPBearer(auto_error=False)


def _unauthorized() -> HTTPException:
    return HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail=ErrorMessages.INVALID_ACCESS_TOKEN,
        headers={'WWW-Authenticate': 'Bearer'},
    )


def get_access_token(authorization: HTTPAuthorizationCredentials | None = Depends(oauth2_scheme)) -> str:
    if not authorization:
        raise _unauthorized()
    return authorization.credentials


def validate_access_token(
    token: str = Depends(get_access_token),
) -> dict[str, Any]:
    unauthorized_exc = _unauthorized()

    try:
        token_data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=settings.ALGORITHM,
            options={'verify_signature': True, 'verify_exp': True, 'require': ['sub', 'exp']},
        )

    except jwt.InvalidTokenError as err:
        logger.warning(err)
        raise unauthorized_exc

    else:
        return token_data


async def get_current_user(
    token_payload: dict[str, Any] = Depends(validate_access_token),
    user_service: UserService = Depends(get_user_service),
) -> User:
    user_id = int(token_payload['sub'])
    return await user_service.get_user_by_id(user_id)
