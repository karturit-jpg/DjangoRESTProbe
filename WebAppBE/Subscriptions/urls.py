from .views import *
from django.urls import path

urlpatterns = [
    path('api/v1/ListTariffs', ListTariffs.as_view()),
    path('api/v1/ManopulateSubscription/<int:pk>/', ManipulateObjectSubscriptions.as_view()),
]