from django.contrib import admin
from .models import *

admin.site.register(Subscription)
admin.site.register(Tariff)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'start_date' ,'is_active', 'fk_user')
    list_editable = ('fk_user',)

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'fk_subscription')
    list_editable = ('fk_subscription',)