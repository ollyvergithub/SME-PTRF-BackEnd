import json

import pytest
from rest_framework import status

from ...api.serializers import ReceitaListaSerializer
from ...models import Receita

pytestmark = pytest.mark.django_db


def test_api_conciliar_receita_sem_periodo(jwt_authenticated_client_p, receita_nao_conferida):
    receita_uuid = receita_nao_conferida.uuid

    url = f'/api/receitas/{receita_uuid}/conciliar/'

    response = jwt_authenticated_client_p.patch(url, content_type='application/json')

    result = json.loads(response.content)

    esperado = {
        'erro': 'parametros_requerido',
        'mensagem': 'É necessário enviar o uuid do período onde esta sendo feita a conciliação.'
    }

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert result == esperado


def test_api_conciliar_receita_com_periodo(jwt_authenticated_client_p, receita_nao_conferida, periodo_2020_1):
    receita_uuid = receita_nao_conferida.uuid

    url = f'/api/receitas/{receita_uuid}/conciliar/?periodo={periodo_2020_1.uuid}'

    response = jwt_authenticated_client_p.patch(url, content_type='application/json')

    result = json.loads(response.content)

    receita_conciliada = Receita.by_uuid(receita_uuid)
    result_esperado = ReceitaListaSerializer(receita_conciliada, many=False).data

    # Converte campos não string em strings para que a comparação funcione
    result_esperado['uuid'] = f'{result_esperado["uuid"]}'
    result_esperado['data'] = f'{result_esperado["data"]}'

    assert response.status_code == status.HTTP_200_OK
    assert result == result_esperado

    assert receita_conciliada.conferido, "Receita deveria ter sido marcada como conferida."
    assert receita_conciliada.periodo_conciliacao == periodo_2020_1, "Receita deveria ter sido vinculada ao período."
