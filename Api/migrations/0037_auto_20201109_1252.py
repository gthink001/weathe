# Generated by Django 3.1.3 on 2020-11-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0036_auto_20201109_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='Response',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
