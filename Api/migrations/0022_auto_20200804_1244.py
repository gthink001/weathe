# Generated by Django 3.0.6 on 2020-08-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0021_auto_20200804_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittertreeuser',
            name='TreeTwitterUserId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='twittertreeuser',
            name='TreeTwitterUserTag',
            field=models.CharField(max_length=50),
        ),
    ]