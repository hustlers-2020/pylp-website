# Generated by Django 2.1.10 on 2020-08-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20200810_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_user',
        ),
    ]