# Generated by Django 2.2.2 on 2019-08-21 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserTable',
        ),
    ]
