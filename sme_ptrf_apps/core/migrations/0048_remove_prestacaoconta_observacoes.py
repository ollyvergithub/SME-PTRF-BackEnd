# Generated by Django 2.2.10 on 2020-07-02 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_observacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestacaoconta',
            name='observacoes',
        ),
    ]
