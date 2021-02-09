import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from model_bakery import baker

from ...models.arquivo import CARGA_ASSOCIACOES, DELIMITADOR_VIRGULA, DELIMITADOR_PONTO_VIRGULA

pytestmark = pytest.mark.django_db


@pytest.fixture
def arquivo():
    return SimpleUploadedFile(
        f'arquivo.csv',
        bytes(f"""Código eol,Conta,Ação,Referência Período, Valor capital,Valor custeio,Valor livre aplicacao\n93238,Cheque,Role Cultural,2020.u,99000.98,99000.98,""", encoding="utf-8"))


@pytest.fixture
def arquivo2():
    return SimpleUploadedFile(
        f'arquivo2.csv',
        bytes(f"""Código eol,Conta,Ação,Referência Período, Valor capital,Valor custeio,Valor livre aplicacao\n93238,Cheque,Role Cultural,2020.u,99000.98,99000.98,""", encoding="utf-8"))


@pytest.fixture
def arquivo_associacao():
    return SimpleUploadedFile(
        f'arquivo.csv',
        bytes(f"""Código EOL UE;Nome UE;Código EOL DRE;Nome da DRE UE;Sigla DRE;Nome da associação;CNPJ da associação;RF Presidente Diretoria;Nome Presidente Diretoria;RF Presidente Conselho Fiscal;Nome Presidente Conselho Fiscal
000086;EMEI PAULO CAMILHIER FLORENCANO;108500;GUAIANASES;G;EMEI PAULO CAMILHIER FLORENÇANO;1142145000190;;;;
000108;"EMEF JOSE ERMIRIO DE MORAIS; SEN.";109300;SAO MIGUEL;MP;EMEF SEN JOSÉ ERMINIO DE MORAIS;1095757000179;;;;""", encoding="utf-8"))


@pytest.fixture
def arquivo_carga(arquivo):
    return baker.make(
        'Arquivo',
        identificador='carga_previsao_repasse',
        conteudo=arquivo,
        tipo_carga=CARGA_ASSOCIACOES,
        tipo_delimitador=DELIMITADOR_VIRGULA,
    )


@pytest.fixture
def arquivo_carga_associacao(arquivo_associacao):
    return baker.make(
        'Arquivo',
        identificador='carga_associacao',
        conteudo=arquivo_associacao,
        tipo_carga=CARGA_ASSOCIACOES,
        tipo_delimitador=DELIMITADOR_PONTO_VIRGULA,
    )

