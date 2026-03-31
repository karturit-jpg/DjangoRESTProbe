from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from datetime import timedelta # почему некоторые пакеты нужно скачивать, а другие достаточно упомянуть?


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True, unique=True)
    telegram_id = models.BigIntegerField(blank=True, null=True, default=None, unique=True)

    def __str__(self):
        return f"{self.username} - {self.phone_number}"


class TelegramBindCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)