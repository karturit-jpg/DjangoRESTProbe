from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Subscription # почему здесь избыточно обственноручно импортировать Тариф и Подписку?
from .serializers import *
from .permissions import *


class ListTariffs(generics.ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = ( AllowAny, )


class ManipulateObjectSubscriptions(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all() # то есть либо можно переопределить queryset в методе get_queryset, либо уже к нему описать желанные ограничения? # в такой реализации, тсало быть, я его переопределил и потому строка избыточна, но в предложении ai-помощника она была бы заиспользована?
    serializer_class = SubscriptionSerializer
    permission_classes = ( EitherIsAdminThenAllowAnyOrIsOwnerThenAllowSafe,  )

    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            return Subscription.objects.all() # почему нейросеть предложила это выражение? << self.queryset.all() >>. Что за self.queryset?
        return Subscription.queryset.filter(user=user)


    # дефолтные Permission-классы определяют доступ к ( методам, определенным во вью, + записям об инстансах ), одновременно
    # ограничить доступ к обьектам, исключая переопределение доступа к методам, можно самостоятельно определив каcтомный Permission-класс с расписанным методом has_object_permission
    # чтобы определить режим доступа к методам, определенным для класса-viewset'а, независимо от права для получения доступа к обьекту, можно ??
    # чтобы комбинировать ограничения доступа по методу и по обьекту, следует определять метод класса viewset'а get_queryset, в котором уже самостоятельно озоботиться проверками метода запроса, переданного в данный get_queryset и отношением пользователя, инициировавшего запрос, и записи, к которой он вызывает
    # но если я хочу оставить за администратором права на доступ ко всем обьектам, всеми методами по типу << permission_classes = ( IsAdminUser,  ) >> и вместе с тем ограничить право пользователя на двух уровнях (метод+обьект), как тогда валидно расписать комбинацию этих логик?

    # чтобы не писать каждый раз permission_classes, можно наследоваться от класса, который уже содержит нужные permission_classes --комментарий ai, правда ли?