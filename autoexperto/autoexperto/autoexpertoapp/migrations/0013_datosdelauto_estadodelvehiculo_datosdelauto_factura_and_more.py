# Generated by Django 4.1.6 on 2023-03-03 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpertoapp', '0012_datosdelauto_imagen2_datosdelauto_imagen3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosdelauto',
            name='estadodelvehiculo',
            field=models.CharField(max_length=200, null=True, verbose_name='estadodelvehiculo'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='factura',
            field=models.CharField(max_length=200, null=True, verbose_name='factura'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='kilometraje',
            field=models.CharField(max_length=200, null=True, verbose_name='kilometraje'),
        ),
        migrations.AddField(
            model_name='datosdelauto',
            name='numerodedueno',
            field=models.CharField(max_length=200, null=True, verbose_name='numerodedueno'),
        ),
    ]
