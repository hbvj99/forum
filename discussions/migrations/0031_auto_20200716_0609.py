# Generated by Django 3.0.7 on 2020-07-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0030_auto_20200716_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='img',
            field=models.ImageField(blank=True, default='/static/image/user/default-user.svg', null=True, upload_to='images/discussion/%Y/%m/%d/'),
        ),
    ]