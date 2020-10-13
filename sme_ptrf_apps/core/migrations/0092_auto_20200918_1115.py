# Generated by Django 2.2.10 on 2020-09-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_remove_ata_conta_associacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ata',
            name='parecer_conselho',
            field=models.CharField(choices=[('APROVADA', 'Aprovada'), ('REJEITADA', 'Rejeitada')], default='APROVADA', max_length=20, verbose_name='parecer do conselho'),
        ),
        migrations.AlterField(
            model_name='prestacaoconta',
            name='status',
            field=models.CharField(choices=[('DOCS_PENDENTES', 'Documentos pendentes'), ('NAO_RECEBIDA', 'Não recebida'), ('RECEBIDA', 'Recebida'), ('EM_ANALISE', 'Em análise'), ('DEVOLVIDA', 'Devolvida para acertos'), ('APROVADA', 'Aprovada'), ('APROVADA_RESSALVA', 'Aprovada com ressalvas'), ('REPROVADA', 'Reprovada')], default='DOCS_PENDENTES', max_length=15, verbose_name='status'),
        ),
    ]
