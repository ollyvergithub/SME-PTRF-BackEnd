# Generated by Django 2.2.10 on 2020-09-02 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_delete_observacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestacaoconta',
            name='conciliado',
        ),
        migrations.RemoveField(
            model_name='prestacaoconta',
            name='conciliado_em',
        ),
    ]