# Generated by Django 3.1 on 2020-09-07 02:29

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0025_auto_20200827_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='CkeditorMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ckeditor_media/', validators=[news.models.validate_image_size])),
            ],
        ),
    ]