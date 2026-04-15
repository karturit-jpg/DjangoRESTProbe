from rest_framework import serializers

from .models import Subscription, Tariff #  здесь уже импорты нужны--не как во вью


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
    # для записей об инстансах этого класса уже админ передает id пользователя, thus не определяю hiddenfield=CurrentUser()


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'