# Generated by Django 3.1 on 2020-08-19 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200819_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.cluster'),
        ),
    ]
