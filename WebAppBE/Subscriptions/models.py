from django.contrib.auth import get_user_model
from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=30)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True) # продлена? приостановлена?
    fk_user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True) # пускай пользователь может одновременно иметь только одну из независимо от него определенных подпискок

    def __str__(self):
        return self.name


class Tariff(models.Model):
    name = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)
    fk_subscription = models.ForeignKey("Subscription", on_delete=models.SET_NULL, null=True, blank=True) # у одной подписки будет один из тарифов

    def __str__(self):
        return self.name