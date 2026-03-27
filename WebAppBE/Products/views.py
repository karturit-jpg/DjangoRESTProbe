from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrDenyAccess
from .models import Order
from .serializers import *

class ManipulateObjectOrder(generics.RetrieveUpdateDestroyAPIView): # можно разбить на классы по заголовку, целесообразно ли?
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_classes = ( IsAuthenticated, IsOwnerOrDenyAccess ) # валидирует по двум критериям, как если бы условия были обьединены "AND"?