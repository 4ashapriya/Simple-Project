# Generated by Django 3.1.6 on 2021-02-09 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
