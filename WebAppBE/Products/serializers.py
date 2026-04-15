from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) # не записал этот прием в REST'е: какаво логика (как с ним работать и что он значит)? --FE будет передавать json без аттрибута, а BE его сгенерирует; и обратно по оси: BE не станет упомянать аттрибут в json'е?
    class Meta:
        model = Order
        fields = '__all__'