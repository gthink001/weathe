# Generated by Django 2.1.7 on 2020-04-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_auto_20200405_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Heavy_State',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]