import json

import pytest

from rest_framework import status

pytestmark = pytest.mark.django_db


def test_api_acoes_list(jwt_authenticated_client_a, acao_x, acao_y):
    response = jwt_authenticated_client_a.get(f'/api/acoes/', content_type='application/json')
    result = json.loads(response.content)

    resultado_esperado = [
        {
            'id': acao_x.id,
            'nome': 'X',
            'uuid': f'{acao_x.uuid}',
            'e_recursos_proprios': False,
            'posicao_nas_pesquisas': 'ZZZZZZZZZZ',
        },
        {
            'id': acao_y.id,
            'nome': 'Y',
            'uuid': f'{acao_y.uuid}',
            'e_recursos_proprios': False,
            'posicao_nas_pesquisas': 'ZZZZZZZZZZ',

        }
    ]

    assert response.status_code == status.HTTP_200_OK
    assert result == resultado_esperado


def test_api_acoes_list_por_nome(jwt_authenticated_client_a, acao_xpto, acao_y):
    response = jwt_authenticated_client_a.get(f'/api/acoes/?nome=P', content_type='application/json')
    result = json.loads(response.content)

    resultado_esperado = [
        {
            'id': acao_xpto.id,
            'nome': 'Xpto',
            'uuid': f'{acao_xpto.uuid}',
            'e_recursos_proprios': False,
            'posicao_nas_pesquisas': 'ZZZZZZZZZZ',
        },
    ]

    assert response.status_code == status.HTTP_200_OK
    assert result == resultado_esperado
