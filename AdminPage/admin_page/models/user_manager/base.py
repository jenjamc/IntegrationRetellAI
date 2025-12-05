from datetime import datetime
from datetime import timezone

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from admin_page.settings.db import db


def utc_now():
    return datetime.now(tz=timezone.utc)


class BaseModel(db.Model):
    __abstract__ = True
    __bind_key__ = 'user_manager'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(default=utc_now, onupdate=utc_now)
