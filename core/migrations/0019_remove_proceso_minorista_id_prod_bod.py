# Generated by Django 3.1 on 2020-10-26 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201025_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proceso_minorista',
            name='id_prod_bod',
        ),
    ]