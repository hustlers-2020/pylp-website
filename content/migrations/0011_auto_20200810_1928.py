# Generated by Django 3.1 on 2020-08-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20180916_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directory',
            options={'verbose_name': 'Directory Entry', 'verbose_name_plural': 'Directory Entries'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
    ]