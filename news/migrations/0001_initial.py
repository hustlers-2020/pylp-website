# Generated by Django 2.1 on 2018-08-10 05:04

from django.db import migrations, models
import news.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to=news.models.get_image_path)),
            ],
            options={
                'verbose_name': 'News Article',
                'verbose_name_plural': 'News Articles',
            },
        ),
    ]
