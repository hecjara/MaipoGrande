# Generated by Django 3.1 on 2020-11-05 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_estado_poliza'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguro',
            name='id_estado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.estado_poliza'),
            preserve_default=False,
        ),
    ]
