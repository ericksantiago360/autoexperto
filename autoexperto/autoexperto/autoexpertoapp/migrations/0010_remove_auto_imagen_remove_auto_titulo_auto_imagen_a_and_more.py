# Generated by Django 4.1.6 on 2023-02-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpertoapp', '0009_rename_auto_auto_datos_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='auto',
            name='titulo',
        ),
        migrations.AddField(
            model_name='auto',
            name='imagen_a',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen_a'),
        ),
        migrations.AddField(
            model_name='auto',
            name='imagen_b',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen_b'),
        ),
        migrations.AddField(
            model_name='auto',
            name='imagen_c',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen_c'),
        ),
        migrations.AddField(
            model_name='auto',
            name='imagen_d',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen_d'),
        ),
    ]
