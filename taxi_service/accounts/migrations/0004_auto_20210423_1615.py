# Generated by Django 3.2 on 2021-04-23 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_dispatcher_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='dispatcher',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='dispatcher',
            name='user_permissions',
        ),
    ]