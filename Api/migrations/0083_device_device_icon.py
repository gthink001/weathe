# Generated by Django 3.1.2 on 2022-11-13 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0082_auto_20220923_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Device_Icon',
            field=models.CharField(blank=True, default='["https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg","https://gthink-images-website.s3.ap-south-1.amazonaws.com/svg/bulb01.svg"]', max_length=2256, null=True),
        ),
    ]
