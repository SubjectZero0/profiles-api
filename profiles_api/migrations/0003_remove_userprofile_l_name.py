# Generated by Django 4.1 on 2022-09-25 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_rename_f_name_userprofile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='l_name',
        ),
    ]
