import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .services import send_telegram_message

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Order)
def notify_about_new_order(sender, instance, created, **kwargs):
    if not created:
        return

    telegram_id = getattr(instance.user, "telegram_id", None)
    if not telegram_id:
        return

    success = send_telegram_message(
        chat_id=telegram_id,
        text=f"You have a new order: #{instance.pk}"
    )

    if not success:
        logger.warning(
            "Failed to send Telegram message for order %s",
            instance.pk
        )