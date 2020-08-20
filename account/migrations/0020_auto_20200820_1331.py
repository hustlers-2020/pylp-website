# Generated by Django 3.1 on 2020-08-20 05:31

import account.models
from django.db import migrations, models
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20200820_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=functools.partial(account.models._update_filename, *(), **{'path': 'photos'}), verbose_name='Profile Picture'),
        ),
    ]
