import toml


def get_version_and_project_name(file_path: str) -> tuple[str, str]:
    with open(file_path, 'r') as file:
        data = toml.load(file)
    version = data['tool']['poetry']['version']
    project_name = data['tool']['poetry']['name']
    return version, project_name
