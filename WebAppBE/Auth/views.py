from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import random
import json

import WebAppBE
from WebAppBE.settings import BASE_DIR
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


@csrf_exempt # так, защиту гарантировал бы кастомный класс фрейворка (скорее всего, логика была определена в его родителях) и он бы генерировал ошибки, но решив написать функцию, и самостоятельно, пришлось указать код технических аспектов (eg, роверку токена) в теле функции; и так, все, кроме бизнес-алгоритма в функции, --код, являющий прекрасный пример, что демонстрируюет сколько логики сокрыто в коробочном классе фрейворка
def bind_telegram_account(request): # в качестве примера концепта, как разрешить обращаться к этому методу только сервису бота?

    if request.headers.get("X-Bot-Secret") != WebAppBE.settings.BOT_API_SECRET: # записать как пример синтаксиса импорта в проекте со сложной иерархией каталогов
        return JsonResponse(
            {"status": "error", "message": "Forbidden."},
            status=403,
        )
    # фрагмент выше и ассоциированная логика гарантируют, что слать запросы можно только через телеграм бота, только с того пользователя которым авторизован; сравни с доступностью относительно запросов с рисованными json'ами через Postman

    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "Only POST is allowed."},
            status=405
        )

    try: # когда это не мой собстевнноручно написанный функционал генерирует обьекты, и/или то есть сведения, переданные третьей стороной, всегда пиши экстракты из них и манипуляции под try-except
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

    if CustomUser.objects.filter(telegram_id=telegram_id).exclude(pk=user.pk).exists(): # чудесный пример QuerySet'а
        return JsonResponse(
            {"status": "error", "message": "This Telegram account is already linked to another user."},
            status=400
        )

    user.telegram_id = telegram_id
    user.save(update_fields=["telegram_id"]) # передает параметры методу save--для чего? --чтобы не обновлять все поля модели, а только те, которые указаны в списке update_fields?

    bind_code.is_used = True
    bind_code.save(update_fields=["is_used"])

    return JsonResponse({
        "status": "ok",
        "message": "Telegram account successfully linked."
    })