# Generated by Django 2.1 on 2018-08-10 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date_uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
