# Generated by Django 3.0.7 on 2020-07-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200716_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/user/%Y/%m/%d/'),
        ),
    ]
