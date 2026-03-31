from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import random
import json

from .models import TelegramBindCode, CustomUser


@login_required
def generate_telegram_code(request):
    code = str(random.randint(100000, 999999))

    TelegramBindCode.objects.create(
        user=request.user,
        code=code
    )

    return JsonResponse({
        "code": code,
        "message": "Send this code to the Telegram bot within 10 minutes."
    })


@csrf_exempt
def bind_telegram_account(request): # в качестве примера концепта, как разрешить обращаться к этому методу только сервису бота?
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "Only POST is allowed."},
            status=405
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON."},
            status=400
        )

    code = str(data.get("code", "")).strip()
    telegram_id = data.get("telegram_id")

    if not code or telegram_id is None:
        return JsonResponse(
            {"status": "error", "message": "Both code and telegram_id are required."},
            status=400
        )

    try:
        bind_code = TelegramBindCode.objects.select_related("user").get(
            code=code,
            is_used=False,
        )
    except TelegramBindCode.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Invalid or already used code."},
            status=404
        )

    if bind_code.is_expired():
        return JsonResponse(
            {"status": "error", "message": "Code has expired."},
            status=400
        )

    user = bind_code.user

    if user.telegram_id is not None and user.telegram_id != telegram_id:
        return JsonResponse(
            {"status": "error", "message": "This user is already linked to another Telegram account."},
            status=400
        )

    if CustomUser.objects.filter(telegram_id=telegram_id).exclude(pk=user.pk).exists():
        return JsonResponse(
            {"status": "error", "message": "This Telegram account is already linked to another user."},
            status=400
        )

    user.telegram_id = telegram_id
    user.save(update_fields=["telegram_id"])

    bind_code.is_used = True
    bind_code.save(update_fields=["is_used"])

    return JsonResponse({
        "status": "ok",
        "message": "Telegram account successfully linked."
    })