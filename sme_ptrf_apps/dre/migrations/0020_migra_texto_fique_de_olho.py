# Generated by Django 2.2.10 on 2020-12-29 11:22

from django.db import migrations


def migrate_data(apps, schema_editor):
    model_parametros = apps.get_model('core', 'Parametros')
    model_parametro_fique_de_olho_rel_dre = apps.get_model('dre', 'ParametroFiqueDeOlhoRelDre')
    fique_de_olho_texto = model_parametros.objects.get().fique_de_olho_relatorio_dre
    model_parametro_fique_de_olho_rel_dre.objects.create(fique_de_olho=fique_de_olho_texto)


class Migration(migrations.Migration):

    dependencies = [
        ('dre', '0019_parametrofiquedeolhoreldre'),
    ]

    operations = [
        migrations.RunPython(migrate_data, reverse_code=migrations.RunPython.noop)
    ]
