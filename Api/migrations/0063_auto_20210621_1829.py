# Generated by Django 3.1.2 on 2021-06-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0062_auto_20210621_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irbuttoninfo',
            name='IRType',
            field=models.TextField(max_length=56),
        ),
        migrations.AlterField(
            model_name='irroominfo',
            name='IRType',
            field=models.TextField(max_length=56),
        ),
    ]