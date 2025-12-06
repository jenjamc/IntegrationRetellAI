import toml

from user_manager.settings.conf import Env
from user_manager.settings.conf import settings


def get_version_and_project_name(file_path: str) -> tuple[str, str]:
    if settings.ENV == Env.TESTING:
        return '0.0.0', 'user_manager'

    with open(file_path, 'r') as file:
        data = toml.load(file)
    version = data['tool']['poetry']['version']
    project_name = data['tool']['poetry']['name']
    return version, project_name
