# Generated by Django 2.2.10 on 2020-05-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_prestacaoconta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestacaoconta',
            name='status',
            field=models.CharField(choices=[('ABERTO', 'Aberta'), ('FECHADO', 'Fechada')], default='ABERTO', max_length=15, verbose_name='status'),
        ),
    ]
