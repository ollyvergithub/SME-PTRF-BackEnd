# Generated by Django 2.2.10 on 2020-08-12 08:40

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_unidade_dre_designacao_ano'),
        ('dre', '0003_auto_20200811_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificacaoRegularidadeAssociacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('regular', models.BooleanField(default=True, verbose_name='Regular?')),
                ('associacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='verificacoes_regularidade', to='core.Associacao')),
                ('grupo_verificacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='grupos_de_verificacao', to='dre.GrupoVerificacaoRegularidade')),
                ('item_verificacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itens_de_verificacao', to='dre.ItemVerificacaoRegularidade')),
                ('lista_verificacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='listas_de_verificacao', to='dre.ListaVerificacaoRegularidade')),
            ],
            options={
                'verbose_name': 'Verificação de regularidade de associação',
                'verbose_name_plural': 'Verificações de regularidade de associações',
            },
        ),
    ]
