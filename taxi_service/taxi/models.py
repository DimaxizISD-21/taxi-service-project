from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class TaxiAuto(models.Model):
    model_name = models.CharField(max_length=50, verbose_name='Модель авто')
    taxi_status = models.BooleanField(max_length=10, default=True, verbose_name='Статус')

    class Meta:
        verbose_name='Такси'
        verbose_name_plural='Список такси'

    def __str__(self):
        return self.model_name


class TaxiOrder(models.Model):
    client_name = models.CharField(max_length=50, verbose_name='Имя')
    phone_number = PhoneNumberField(blank=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адресс назначения')
    desired_time = models.TimeField(verbose_name='Желаемое время')
    taxi_auto = models.ForeignKey(TaxiAuto, on_delete=models.CASCADE, verbose_name='Модель авто')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Список заказов'

    def __str__(self):
        return f'Заказ №{self.id}'



