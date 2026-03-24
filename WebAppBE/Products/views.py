from rest_framework import generics
from .models import Order
from .serializers import *

class ManipulateObjectOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer