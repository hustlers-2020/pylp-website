# Generated by Django 2.1 on 2018-09-12 10:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180912_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]