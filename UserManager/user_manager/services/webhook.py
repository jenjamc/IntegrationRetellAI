import json
from typing import Any

from retell import Retell

from user_manager import settings


class WebhookService:
    def __init__(self):
        self.client = Retell(
            api_key=settings.RETELL_WEBHOOK_KEY,
            timeout=20.0,
        )

    def verify_webhook(self, post_data: Any, signature: str) -> bool:
        return self.client.verify(
            json.dumps(post_data, separators=(',', ':'), ensure_ascii=False),
            api_key=settings.RETELL_WEBHOOK_KEY,
            signature=signature,
        )
