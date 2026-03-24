from .views import *
from django.urls import path

urlpatterns = [
    path('api/v1/ManipulateOrder/<int:pk>/', ManipulateObjectOrder.as_view()),
]