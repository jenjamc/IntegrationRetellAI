from datetime import datetime
from datetime import timezone

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from admin_page import settings

metadata = MetaData()

Base = declarative_base(metadata=metadata)


def utc_now():
    return datetime.now(tz=timezone.utc)


class BaseModel(Base):
    __abstract__ = True
    __bind_key__ = settings.DB_NAME_ADMIN_PAGE

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(default=utc_now, onupdate=utc_now)
