# Generated by Django 3.0.6 on 2020-07-17 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0017_auto_20200717_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treeemploy',
            old_name='EmployParent',
            new_name='EmployNumber',
        ),
    ]