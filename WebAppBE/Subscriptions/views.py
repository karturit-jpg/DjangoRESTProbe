from rest_framework import generics
from .models import Subscription
from .serializers import *

class ListTariffs(generics.ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class ManipulateObjectSubscriptions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer