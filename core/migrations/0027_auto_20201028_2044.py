# Generated by Django 3.1 on 2020-10-28 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20201028_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='id_estado_pro',
        ),
        migrations.DeleteModel(
            name='ESTADO_PRODUCTO_CARRITO',
        ),
    ]