# Generated by Django 2.1 on 2018-08-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_date_uploaded'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='news_header/')),
            ],
        ),
    ]
