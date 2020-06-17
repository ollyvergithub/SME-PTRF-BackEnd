import pytest
from django.contrib import admin

from ...models import PrestacaoConta, Associacao, Periodo, ContaAssociacao, Ata

pytestmark = pytest.mark.django_db


def test_instance_model(ata_2020_1_cheque_aprovada):
    model = ata_2020_1_cheque_aprovada
    assert isinstance(model, Ata)
    assert isinstance(model.prestacao_conta, PrestacaoConta)
    assert isinstance(model.associacao, Associacao)
    assert isinstance(model.periodo, Periodo)
    assert isinstance(model.conta_associacao, ContaAssociacao)
    assert model.tipo_ata
    assert model.tipo_reuniao
    assert model.convocacao
    assert model.data_reuniao
    assert model.local_reuniao
    assert model.presidente_reuniao
    assert model.cargo_presidente_reuniao
    assert model.secretario_reuniao
    assert model.cargo_secretaria_reuniao
    assert model.comentarios
    assert model.parecer_conselho
    assert model.criado_em
    assert model.alterado_em
    assert model.uuid
    assert model.id


def test_srt_model(ata_2020_1_cheque_aprovada):
    assert ata_2020_1_cheque_aprovada.__str__() == 'Ata 2020.1 - Cheque - ORDINARIA'


def test_meta_modelo(ata_2020_1_cheque_aprovada):
    assert ata_2020_1_cheque_aprovada._meta.verbose_name == 'Ata'
    assert ata_2020_1_cheque_aprovada._meta.verbose_name_plural == 'Atas'


def test_admin():
    # pylint: disable=W0212
    assert admin.site._registry[Ata]

def test_iniciar_ata(prestacao_conta_2020_1_conciliada):
    ata = Ata.iniciar(prestacao_conta_2020_1_conciliada)
    assert ata.prestacao_conta == prestacao_conta_2020_1_conciliada
    assert ata.periodo == prestacao_conta_2020_1_conciliada.periodo
    assert ata.associacao == prestacao_conta_2020_1_conciliada.associacao
    assert ata.conta_associacao == prestacao_conta_2020_1_conciliada.conta_associacao