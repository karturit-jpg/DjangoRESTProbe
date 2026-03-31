from .views import * # nb, синтаксис обращения к импортированным обьектам при написании " from .views import * " и " from . import views " будет различным
from django.urls import path


urlpatterns = [
    path('api/v1/GenerateBindCode/', generate_telegram_code, name='generate_telegram_code'),
]