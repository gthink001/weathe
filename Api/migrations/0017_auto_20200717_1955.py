# Generated by Django 3.0.6 on 2020-07-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0016_auto_20200716_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treeemploy',
            name='id',
        ),
        migrations.AlterField(
            model_name='treeemploy',
            name='EmployParent',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, unique=True),
        ),
    ]