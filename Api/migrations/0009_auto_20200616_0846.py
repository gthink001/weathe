# Generated by Django 3.0.6 on 2020-06-16 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_device_heavy_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='Devicedata',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Devicenumber',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Deviceparent',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Recorddata',
        ),
    ]