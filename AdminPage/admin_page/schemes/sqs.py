from enum import StrEnum

from pydantic import BaseModel

from admin_page.settings.constants import StateTokenizationSnapshot


class NotificationType(StrEnum):
    TOKENIZATION_SNAPSHOT = 'TOKENIZATION_SNAPSHOT'


class SnapshotStateChangedPayloadSchema(BaseModel):
    user_id: int
    state: StateTokenizationSnapshot
    comment: str = ''


class NotificationMessageSchema(BaseModel):
    type: NotificationType
    payload: SnapshotStateChangedPayloadSchema
