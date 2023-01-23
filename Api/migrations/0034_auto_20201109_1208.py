# Generated by Django 3.1.3 on 2020-11-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0033_remoteackey_remoteactwo_remotecompanyname_remoteproductname_remotetvkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remoteproductname',
            name='created_by_id',
        ),
        migrations.RemoveField(
            model_name='remoteproductname',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='remoteproductname',
            name='updated_by_id',
        ),
        migrations.RemoveField(
            model_name='remoteproductname',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='remoteproductname',
            name='product_name',
            field=models.CharField(blank=True, max_length=1800, null=True, unique=True),
        ),
    ]
