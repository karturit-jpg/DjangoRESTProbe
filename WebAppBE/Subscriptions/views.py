from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Subscription
from .serializers import *

class ListTariffs(generics.ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permissions_classes = ( IsAdminUser, )


class ManipulateObjectSubscriptions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permissions_classes = ( IsAdminUser, )