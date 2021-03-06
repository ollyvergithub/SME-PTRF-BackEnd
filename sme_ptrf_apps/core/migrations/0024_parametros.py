# Generated by Django 2.2.10 on 2020-06-02 12:01

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_demonstrativofinanceiro_acao_associacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('permite_saldo_conta_negativo', models.BooleanField(default=True, verbose_name='Permite saldo negativo em contas?')),
            ],
            options={
                'verbose_name': 'Parâmetro',
                'verbose_name_plural': 'Parâmetros',
            },
        ),
    ]
