# Generated by Django 3.1 on 2020-10-12 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_tipo_proceso_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='HISTORIAL_MINORISTA',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('oferta', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('fecha_oferta', models.DateTimeField()),
                ('id_proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proceso_venta')),
                ('id_prod_bod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto_bodega')),
            ],
        ),
    ]