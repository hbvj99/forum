# Generated by Django 3.0.7 on 2020-07-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200716_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/user/default-user.svg', upload_to='images/user/%Y/%m/%d/'),
        ),
    ]
