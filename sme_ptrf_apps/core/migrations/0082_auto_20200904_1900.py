# Generated by Django 2.2.10 on 2020-09-04 19:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_auto_20200902_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoNotificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de notificação',
                'verbose_name_plural': 'Tipos de notificação',
            },
        ),
        migrations.AlterField(
            model_name='prestacaoconta',
            name='status',
            field=models.CharField(choices=[('DOCS_PENDENTES', 'Documentos pendentes'), ('NAO_RECEBIDA', 'Não recebida'), ('RECEBIDA', 'Recebida'), ('EM_ANALISE', 'Em análise'), ('DEVOLVIDA', 'Devolvida para acertos'), ('APROVADA', 'Aprovada'), ('REPROVADA', 'Reprovada')], default='DOCS_PENDENTES', max_length=15, verbose_name='status'),
        ),
    ]