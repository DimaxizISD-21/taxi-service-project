from django.contrib import admin
from taxi.models import TaxiOrder, TaxiAuto

# Register your models here.

@admin.register(TaxiOrder)
class TaxiOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'phone_number', 'address', 'desired_time']


@admin.register(TaxiAuto)
class TaxiAutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_name', 'taxi_status']