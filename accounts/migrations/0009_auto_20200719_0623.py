# Generated by Django 3.0.7 on 2020-07-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200719_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/static/image/default-user.svg', upload_to='images/user/%Y/%m/%d/'),
        ),
    ]
