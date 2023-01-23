# Generated by Django 3.0.6 on 2020-08-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0020_auto_20200803_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TwitterTreeName', models.CharField(max_length=100)),
                ('TwitterTreeParent', models.CharField(max_length=13)),
                ('TwitterTreeId', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreeImage', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreeWeight', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreeHeight', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreeDetails', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreeLocation', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreePlantedDate', models.CharField(blank=True, max_length=254, null=True)),
                ('TwitterTreeState', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterTreeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TreeTwitterUserTag', models.CharField(max_length=50, unique=True)),
                ('TreeTwitterUserId', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('TreeTwitterTagLine', models.CharField(blank=True, max_length=1000, null=True)),
                ('TreeTwitterProfile', models.CharField(blank=True, max_length=100, null=True)),
                ('TreeTwitterCount', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TreeTwitterUser',
        ),
    ]