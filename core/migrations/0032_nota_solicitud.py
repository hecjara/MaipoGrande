# Generated by Django 3.1 on 2020-11-04 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_historial_subasta_id_conclusion'),
    ]

    operations = [
        migrations.CreateModel(
            name='NOTA_SOLICITUD',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.CharField(max_length=2000)),
                ('id_solicitud', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.solicitud_compra')),
            ],
        ),
    ]
