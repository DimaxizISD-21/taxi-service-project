# Generated by Django 3.2 on 2021-04-23 15:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxiAuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50, verbose_name='Модель авто')),
                ('taxi_status', models.BooleanField(default=True, max_length=10, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Такси',
                'verbose_name_plural': 'Список такси',
            },
        ),
        migrations.CreateModel(
            name='TaxiOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адресс назначения')),
                ('desired_time', models.TimeField(verbose_name='Желаемое время')),
                ('taxi_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.taxiauto', verbose_name='Модель авто')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Список заказов',
            },
        ),
    ]
