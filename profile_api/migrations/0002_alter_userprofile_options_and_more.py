# Generated by Django 4.0.4 on 2022-06-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
