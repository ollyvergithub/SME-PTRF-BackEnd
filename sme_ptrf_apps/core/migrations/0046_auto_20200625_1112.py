# Generated by Django 2.2.10 on 2020-06-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_merge_20200624_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membroassociacao',
            name='cargo_associacao',
            field=models.CharField(blank=True, choices=[('PRESIDENTE_DIRETORIA_EXECUTIVA', 'Presidente da diretoria executiva'), ('VICE_PRESIDENTE_DIRETORIA_EXECUTIVA', 'Vice-Presidente da diretoria executiva'), ('SECRETARIO', 'Secretario'), ('TESOUREIRO', 'Tesoureiro'), ('VOGAL_1', 'Vogal 1'), ('VOGAL_2', 'Vogal 2'), ('VOGAL_3', 'Vogal 3'), ('VOGAL_4', 'Vogal 4'), ('VOGAL_5', 'Vogal 5'), ('PRESIDENTE_CONSELHO_FISCAL', 'Presidente do conselho fiscal'), ('CONSELHEIRO_1', 'Conselheiro 1'), ('CONSELHEIRO_2', 'Conselheiro 2'), ('CONSELHEIRO_3', 'Conselheiro 3'), ('CONSELHEIRO_4', 'Conselheiro 4')], default='Presidente da diretoria executiva', max_length=65, null=True, verbose_name='Cargo Associação'),
        ),
        migrations.AlterField(
            model_name='membroassociacao',
            name='representacao',
            field=models.CharField(choices=[('SERVIDOR', 'Servidor'), ('PAI_RESPONSAVEL', 'Pai_ou_responsável'), ('ESTUDANTE', 'Estudante')], default='Servidor', max_length=25, verbose_name='Representação'),
        ),
    ]