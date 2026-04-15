from django.contrib.auth import get_user_model
from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=30)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True) # продлена? приостановлена?
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True) # пускай пользователь может одновременно иметь только одну из независимо от него определенных подпискок
    # сменил имена аттрибутов-внешних ключей; мотивацивию дал Алексей: "ставишь преписку fk_. так делать не рекомендуется потому что если мы залезем в бд то там будет сохранено следующее: название_поля_id,  в котором будет храниться айдишка. так мы и поймем что это foreign key"

    def __str__(self):
        return f"{self.name}" # nb, указал два функционально идентичных способа передать имя обьекта: в этом классе и классе ниже


class Tariff(models.Model):
    name = models.CharField(max_length=100)
    discount = models.IntegerField(default=0)
    fk_subscription = models.ForeignKey("Subscription", on_delete=models.SET_NULL, null=True, blank=True) # у одной подписки будет один из тарифов

    def __str__(self):
        return str(self.name)