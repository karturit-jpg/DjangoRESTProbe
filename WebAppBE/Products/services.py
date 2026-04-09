import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_telegram_message(chat_id: int, text: str) -> bool:
    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
    except requests.RequestException as exc:
        logger.warning("Telegram send failed: %s", exc)
        return False

    return True