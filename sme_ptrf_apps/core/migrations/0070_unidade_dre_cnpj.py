# Generated by Django 2.2.10 on 2020-08-08 13:02

from django.db import migrations, models
import sme_ptrf_apps.core.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_merge_20200807_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidade',
            name='dre_cnpj',
            field=models.CharField(blank=True, default='', max_length=20, null=True, validators=[sme_ptrf_apps.core.models.validators.cnpj_validation], verbose_name='CNPJ da DRE'),
        ),
    ]
