# Generated by Django 3.0.6 on 2020-05-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0011_auto_20200509_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
