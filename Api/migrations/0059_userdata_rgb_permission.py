# Generated by Django 3.1.2 on 2021-04-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0058_auto_20210102_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='Rgb_Permission',
            field=models.CharField(blank=True, max_length=956, null=True),
        ),
    ]