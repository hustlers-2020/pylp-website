# Generated by Django 2.1.10 on 2020-08-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20200811_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
