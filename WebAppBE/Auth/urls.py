from .views import * # nb, синтаксис обращения к импортированным обьектам при написании " from .views import * " и " from . import views " будет различным
from django.urls import path


urlpatterns = [
    path('telegram/generate-code/', generate_telegram_code, name='tg_binding_get'),
    path('api/telegram/bind/', bind_telegram_account, name='tg_binding_post'),
]