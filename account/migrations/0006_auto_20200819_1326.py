# Generated by Django 3.1 on 2020-08-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200819_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='committee',
            field=models.ManyToManyField(blank=True, to='account.Committee'),
        ),
    ]