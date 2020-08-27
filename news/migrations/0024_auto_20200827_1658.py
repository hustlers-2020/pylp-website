# Generated by Django 3.1 on 2020-08-27 08:58

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20200827_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.get_image_path),
        ),
    ]