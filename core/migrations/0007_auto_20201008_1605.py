# Generated by Django 3.1 on 2020-10-08 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201008_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]