import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import TelegramBindCode


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

def check_telegram_code(request, code): # в качестве примера концепта, как разрешить обращаться к этому методу только сервису бота?
    return JsonResponse({
        "valid": TelegramBindCode.objects.filter(code=code).exists()
    })