# Generated by Django 3.0.6 on 2020-05-12 16:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0016_auto_20200512_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='content',
            field=ckeditor.fields.RichTextField(default='content'),
        ),
    ]
