# Generated by Django 3.0.1 on 2020-05-01 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0006_auto_20200501_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='image',
        ),
    ]
