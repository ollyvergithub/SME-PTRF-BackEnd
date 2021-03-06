import json

import pytest
from rest_framework import status

from ...tipos_aplicacao_recurso import APLICACAO_CUSTEIO, APLICACAO_CAPITAL, APLICACAO_NOMES

pytestmark = pytest.mark.django_db


def test_api_get_despesas_tabelas(associacao, jwt_authenticated_client_d, tipo_aplicacao_recurso, tipo_custeio, tipo_documento, tipo_transacao, acao,
                                  acao_associacao, tipo_conta, conta_associacao, tag_ativa):
    response = jwt_authenticated_client_d.get(f'/api/despesas/tabelas/?associacao_uuid={associacao.uuid}', content_type='application/json')
    result = json.loads(response.content)

    esperado = {
        'tipos_aplicacao_recurso': [
            {
                'id': APLICACAO_CAPITAL,
                'nome': APLICACAO_NOMES[APLICACAO_CAPITAL]
            },
            {
                'id': APLICACAO_CUSTEIO,
                'nome': APLICACAO_NOMES[APLICACAO_CUSTEIO]
            }
        ],

        'tipos_custeio': [
            {
                'id': tipo_custeio.id,
                'nome': tipo_custeio.nome,
                'uuid': f'{tipo_custeio.uuid}'
            },
        ],

        'tipos_documento': [
            {
                'id': tipo_documento.id,
                'nome': tipo_documento.nome,
                'apenas_digitos': tipo_documento.apenas_digitos,
                'numero_documento_digitado': tipo_documento.numero_documento_digitado
            },
        ],

        'tipos_transacao': [
            {
                'id': tipo_transacao.id,
                'nome': tipo_transacao.nome,
                'tem_documento': tipo_transacao.tem_documento
            },
        ],

        'acoes_associacao': [
            {
                'uuid': f'{acao_associacao.uuid}',
                'id': acao_associacao.id,
                'nome': acao_associacao.acao.nome,
                'e_recursos_proprios': False

            },
        ],

        'contas_associacao': [
            {
                'uuid': f'{conta_associacao.uuid}',
                'nome': conta_associacao.tipo_conta.nome
            },
        ],

        'tags': [
            {
                'uuid': str(tag_ativa.uuid),
                'nome': tag_ativa.nome,
                'status': tag_ativa.status
            }
        ]
    }

    assert response.status_code == status.HTTP_200_OK
    assert result == esperado


def test_api_get_despesas_tabelas_sem_permissao(associacao, jwt_authenticated_client_sem_permissao, tipo_aplicacao_recurso, tipo_custeio, tipo_documento, tipo_transacao, acao,
                                  acao_associacao, tipo_conta, conta_associacao, tag_ativa):
    response = jwt_authenticated_client_sem_permissao.get(f'/api/despesas/tabelas/?associacao_uuid={associacao.uuid}', content_type='application/json')

    assert response.status_code == status.HTTP_403_FORBIDDEN
