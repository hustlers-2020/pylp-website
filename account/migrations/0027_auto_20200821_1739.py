# Generated by Django 3.1 on 2020-08-21 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_auto_20200820_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityactivity',
            name='activity_description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='communityactivity',
            name='activity_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='communityactivity',
            name='inclusive_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='communityactivity',
            name='profile',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
        migrations.AlterField(
            model_name='communityactivity',
            name='sponsor_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.organization'),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='inclusive_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='level_attained',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='profile',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.school'),
        ),
        migrations.AlterField(
            model_name='membershiporganization',
            name='inclusive_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='membershiporganization',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.organization'),
        ),
        migrations.AlterField(
            model_name='membershiporganization',
            name='position_held',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='membershiporganization',
            name='profile',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]
