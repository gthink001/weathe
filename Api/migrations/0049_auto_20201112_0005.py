# Generated by Django 3.1.3 on 2020-11-12 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0048_remove_device_assigned_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userroominfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]