# Generated by Django 3.1 on 2020-10-12 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCTO_BODEGA',
            fields=[
                ('id_prod_bod', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('precio_estandar', models.IntegerField()),
                ('id_bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bodega')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]