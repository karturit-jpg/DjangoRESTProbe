from rest_framework import serializers

from .models import Subscription, Tariff #  здесь уже импорты нужны--не как во вью


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'