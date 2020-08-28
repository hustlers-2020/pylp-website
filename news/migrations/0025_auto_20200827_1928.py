# Generated by Django 3.1 on 2020-08-27 11:28

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20200827_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.get_image_path, validators=[news.models.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='newslist',
            name='image',
            field=models.ImageField(upload_to='news_header/', validators=[news.models.validate_image_size]),
        ),
    ]
