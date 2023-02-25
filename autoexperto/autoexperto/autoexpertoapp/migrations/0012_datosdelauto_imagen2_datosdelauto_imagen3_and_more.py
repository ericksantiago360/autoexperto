# Generated by Django 4.1.6 on 2023-02-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpertoapp', '0011_datosdelauto_delete_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosdelauto',
            name='imagen2',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen2'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='imagen3',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen3'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='imagen4',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen4'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='marcadelauto',
            field=models.CharField(max_length=200, null=True, verbose_name='marcadelauto'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='modelo',
            field=models.CharField(max_length=200, null=True, verbose_name='modelo'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='precio',
            field=models.CharField(max_length=200, null=True, verbose_name='precio'),
        ),
    ]
