# Generated by Django 3.1 on 2020-10-02 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_compra',
            name='fecha_max',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud_compra',
            name='fecha_min',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
