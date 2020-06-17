# Generated by Django 2.2.10 on 2020-06-11 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_acao_posicao_nas_pesquisas'),
        ('despesas', '0021_despesa_documento_transacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateiodespesa',
            name='prestacao_conta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='despesas_conciliadas', to='core.PrestacaoConta', verbose_name='prestação de contas de conciliação'),
        ),
    ]