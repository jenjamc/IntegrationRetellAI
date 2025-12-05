from admin_page.settings.conf import settings
from admin_page.utilities import get_version_and_project_name

if settings.ENV == 'TESTING':
    file_path = '../pyproject.toml'
else:
    file_path = 'pyproject.toml'

version, project_name = get_version_and_project_name(file_path)
