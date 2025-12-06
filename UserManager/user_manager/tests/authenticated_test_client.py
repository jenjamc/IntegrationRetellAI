# mypy: ignore-errors
from types import TracebackType

from httpx import AsyncClient
from httpx import Response

from user_manager.api.dependencies.auth import get_current_user
from user_manager.models import User


class AuthenticatedTestClient(AsyncClient):
    def __init__(self, user: User, *args, **kwargs):
        super(AuthenticatedTestClient, self).__init__(*args, **kwargs)
        self._user = user

    async def request(self, *args, **kwargs) -> Response:
        headers = kwargs.get('headers') or {}
        headers['Authorization'] = 'Bearer secure_token'
        kwargs['headers'] = headers
        return await super(AuthenticatedTestClient, self).request(*args, **kwargs)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user: User):
        self._user = user

    def _mock_auth_dependency(self):
        self._transport.app.dependency_overrides[get_current_user] = lambda: self.user

    def _unmock_auth_dependency(self):
        if get_current_user in self._transport.app.dependency_overrides:
            del self._transport.app.dependency_overrides[get_current_user]

    async def __aenter__(self):
        self._mock_auth_dependency()
        await super().__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ):
        self._unmock_auth_dependency()
        await super().__aexit__(exc_type, exc_value, traceback)
