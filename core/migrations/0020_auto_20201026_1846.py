# Generated by Django 3.1 on 2020-10-26 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_proceso_minorista_id_prod_bod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='id_prod_proc',
        ),
        migrations.CreateModel(
            name='PRODUCTO_CARRITO',
            fields=[
                ('id_prod_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrito')),
                ('id_prod_proc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto_proceso')),
            ],
        ),
    ]
