# Generated by Django 3.1 on 2020-10-26 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20201026_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='id_prod_proc',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.producto_proceso'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PRODUCTO_CARRITO',
        ),
    ]
