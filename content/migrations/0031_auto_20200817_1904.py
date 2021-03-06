# Generated by Django 3.1 on 2020-08-17 11:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0030_auto_20200817_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='batch_and_year',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='birth_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='birth_place',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='civil_status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='account',
            name='current_work_affiliation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='ethnicity',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='facebook_account',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='host_family',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name_address_office_school',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='permanent_address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='present_address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='religion',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='telephone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
