# Local development

## Setup
We highly recommend to use provided script to setup everything by single command.  
Just run the following command from project's root directory and follow instructions:
* `docker-compose up`

That's all!


## Style guides and name conventions

### Linters and code-formatters
We use git-hooks to run linters and formatters before any commit.
It installs git-hooks automatically if you used `bin/setup` command.
So, if your commit is failed then check console to see details and fix linter issues.

We use:

* black - code formatter
* mypy - static type checker
* flake8 - logical and stylistic lint
* flake8-bandit - security linter
* safety - security check for requirements

and few other flake8 plugins, check `pyproject.toml -> [tool.poetry.group.dev.dependencies]` for more details.

### Poetry

Install deps via poetry

```bash
bin/poetry install  # Install deps
bin/poetry shell  # Activate virtual environment

# Useful commands
bin/poetry add {package_name}  # Add new package to deps with locking
bin/poetry add --group dev {package_name}  # Add new dev package to deps locking
bin/poetry lock  # Update poetry.lock file
bin/poetry update  # Update all deps regarding to the pyproject.toml file
```

### Alembic

Alembic is a lightweight database migration tool for SQLAlchemy.

```bash
bin/alembic  # Show all available commands
bin/alembic revision --autogenerate -m "Add new table"  # Create new migration
bin/alembic upgrade head  # Apply all migrations
bin/alembic downgrade -1  # Rollback last migration
```

### Test

Run pytest

```bash
bin/test  # Run all tests
bin/test {path_to_test_file}  # Run specific test file
bin/test {path_to_test_file}::{test_name}  # Run specific test
```

### Pre-commit

We use pre-commit to run linters and formatters before any commit.

```bash
bin/pre-commit  # Run all pre-commit hooks
```

### Base commands

```bash
docker-compose up  # To run django application server

