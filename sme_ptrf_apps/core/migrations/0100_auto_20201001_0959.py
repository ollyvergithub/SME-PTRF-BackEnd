# Generated by Django 2.2.10 on 2020-10-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0099_analisecontaprestacaoconta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisecontaprestacaoconta',
            name='data_extrato',
            field=models.DateField(blank=True, null=True, verbose_name='data do extrato'),
        ),
    ]