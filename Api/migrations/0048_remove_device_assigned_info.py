# Generated by Django 3.1.3 on 2020-11-11 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0047_device_assigned_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='Assigned_Info',
        ),
    ]