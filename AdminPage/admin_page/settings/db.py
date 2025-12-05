from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from admin_page import settings

admin_engine = create_engine(settings.database_uri + settings.DB_NAME_ADMIN_PAGE)

db = SQLAlchemy()
