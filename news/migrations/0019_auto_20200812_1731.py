# Generated by Django 2.1.10 on 2020-08-12 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20200812_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='banner',
            new_name='image',
        ),
    ]
