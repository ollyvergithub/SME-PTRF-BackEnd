import json

import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_retrieve_acao_associacao(
    jwt_authenticated_client_a,
    acao_associacao_charli_bravo_000086_x
):
    response = jwt_authenticated_client_a.get(
        f'/api/acoes-associacoes/{acao_associacao_charli_bravo_000086_x.uuid}/', content_type='application/json')

    result = json.loads(response.content)

    acao_associacao = acao_associacao_charli_bravo_000086_x

    esperado = {
        'uuid': f'{acao_associacao.uuid}',
        'id': acao_associacao.id,
        'associacao': {
            'uuid': f'{acao_associacao.associacao.uuid}',
            'nome': acao_associacao.associacao.nome,
            'unidade': {
                'uuid': f'{acao_associacao.associacao.unidade.uuid}',
                'codigo_eol': acao_associacao.associacao.unidade.codigo_eol,
                'nome_com_tipo': acao_associacao.associacao.unidade.nome_com_tipo
            },
            'status_regularidade': acao_associacao.associacao.status_regularidade,
        },
        'acao': {
            'id': acao_associacao.acao.id,
            'nome': acao_associacao.acao.nome,
            'e_recursos_proprios': acao_associacao.acao.e_recursos_proprios
        },
        'status': acao_associacao.status,
        'criado_em': acao_associacao.criado_em.isoformat("T"),
    }
    assert response.status_code == status.HTTP_200_OK
    assert result == esperado