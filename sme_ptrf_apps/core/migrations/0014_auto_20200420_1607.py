# Generated by Django 2.2.10 on 2020-04-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_periodo_referencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechamentoperiodo',
            name='status',
            field=models.CharField(choices=[('ABERTO', 'Completo'), ('FECHADO', 'Fechado'), ('IMPLANTACAO', 'Implantação')], default='ABERTO', max_length=15, verbose_name='status'),
        ),
    ]