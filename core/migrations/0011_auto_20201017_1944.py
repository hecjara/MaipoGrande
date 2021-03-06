# Generated by Django 3.1 on 2020-10-17 22:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201014_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONCLUSION',
            fields=[
                ('id_conclusion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='ESTADO_LOTE',
            new_name='ESTADO_PROD_BOD',
        ),
        migrations.RemoveField(
            model_name='producto_bodega',
            name='id_lote',
        ),
        migrations.AddField(
            model_name='producto_bodega',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto_bodega',
            name='fecha_elaboracion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto_bodega',
            name='fecha_vencimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto_bodega',
            name='id_estado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.estado_prod_bod'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto_bodega',
            name='id_producto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto_bodega',
            name='precio_kilo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LOTE',
        ),
        migrations.AddField(
            model_name='historial_postulacion',
            name='id_conclusion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.conclusion'),
        ),
    ]
