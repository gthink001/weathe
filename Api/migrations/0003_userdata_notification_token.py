# Generated by Django 2.1.7 on 2020-04-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20200403_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='Notification_Token',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
