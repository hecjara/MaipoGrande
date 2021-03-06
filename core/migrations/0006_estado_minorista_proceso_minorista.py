# Generated by Django 3.1 on 2020-10-12 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_historial_minorista'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESTADO_MINORISTA',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PROCESO_MINORISTA',
            fields=[
                ('id_proceso', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('id_estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.estado_minorista')),
                ('id_prod_bod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto_bodega')),
            ],
        ),
    ]
