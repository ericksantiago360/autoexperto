# Generated by Django 4.1.6 on 2023-02-22 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpertoapp', '0007_rename_auto_autos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='autos',
            new_name='auto',
        ),
    ]
