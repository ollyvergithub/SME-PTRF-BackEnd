# Generated by Django 2.2.10 on 2020-06-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='tipo_carga',
            field=models.CharField(choices=[('REPASSE_REALIZADO', 'Repasse realizado')], default='REPASSE_REALIZADO', max_length=35, verbose_name='status'),
        ),
    ]
