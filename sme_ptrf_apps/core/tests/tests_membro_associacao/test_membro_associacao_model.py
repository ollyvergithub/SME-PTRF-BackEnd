import pytest

from ...choices import MembroEnum, RepresentacaoCargo
from ...models import MembroAssociacao, Associacao

pytestmark = pytest.mark.django_db


def test_instance_model(membro_associacao):
    model = membro_associacao
    assert isinstance(model, MembroAssociacao)
    assert isinstance(model.associacao, Associacao)
    assert model.nome
    assert model.criado_em
    assert model.uuid
    assert model.cargo_associacao == MembroEnum.PRESIDENTE_DIRETORIA_EXECUTIVA.value
    assert model.representacao == RepresentacaoCargo.SERVIDOR.value
    assert model.email
    assert model.cpf
    assert model.telefone
    assert model.cep
    assert model.bairro
    assert model.endereco


def test_admin():
    from django.contrib import admin
    assert admin.site._registry[MembroAssociacao]
