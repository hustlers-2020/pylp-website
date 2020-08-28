# Generated by Django 3.1 on 2020-08-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0029_educationalbackground_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalbackground',
            name='inclusive_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='level_attained',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='school_address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='school_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
