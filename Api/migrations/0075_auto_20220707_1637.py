# Generated by Django 3.1.2 on 2022-07-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0074_auto_20220227_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealerdevice',
            name='Dealer_customer_number',
        ),
        migrations.RemoveField(
            model_name='dealerdevice',
            name='Dealer_device',
        ),
        migrations.RemoveField(
            model_name='dealerdevice',
            name='Dealer_device_state',
        ),
        migrations.RemoveField(
            model_name='dealerdevice',
            name='Dealer_number',
        ),
        migrations.RemoveField(
            model_name='dealerdevice',
            name='id',
        ),
        migrations.AddField(
            model_name='dealerdevice',
            name='DeviceName',
            field=models.CharField(blank=True, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='dealerdevice',
            name='ParentId',
            field=models.CharField(blank=True, max_length=342, null=True),
        ),
    ]
