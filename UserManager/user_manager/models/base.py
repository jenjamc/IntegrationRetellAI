from datetime import datetime
from datetime import timezone

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


def utc_now():
    return datetime.now(tz=timezone.utc).replace(tzinfo=None)


class BaseModel(Base):  # type: ignore
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(), default=utc_now)
    updated_at = Column(DateTime(), default=utc_now, onupdate=utc_now)
