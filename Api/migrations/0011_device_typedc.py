# Generated by Django 3.0.6 on 2020-06-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0010_device_devicenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='TypedC',
            field=models.CharField(blank=True, max_length=345, null=True),
        ),
    ]
