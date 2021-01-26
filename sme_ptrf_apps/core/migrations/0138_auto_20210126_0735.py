# Generated by Django 2.2.10 on 2021-01-26 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0137_merge_20210114_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acaoassociacao',
            name='acao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='associacoes_da_acao', to='core.Acao'),
        ),
    ]
