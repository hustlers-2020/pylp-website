# Generated by Django 3.1 on 2020-08-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200819_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='committees',
            field=models.ManyToManyField(to='account.Committee'),
        ),
    ]
