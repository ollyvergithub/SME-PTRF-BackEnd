import csv
import datetime
import enum
import logging
import os

from sme_ptrf_apps.core.models import Acao, AcaoAssociacao, Associacao, ContaAssociacao, Periodo, TipoConta
from ..models import Repasse

logger = logging.getLogger(__name__)


class TipoContaEnum(enum.Enum):
    CARTAO = 'Cartão'
    CHEQUE = 'Cheque'

class StatusRepasse(enum.Enum):
    PENDENTE = 'Pendente'
    REALIZADO = 'Realizado'

def get_valor(val):
    if not val:
        return 0

    return float(str(val).replace(',', '.'))


def get_associacao(eol):
    if Associacao.objects.filter(unidade__codigo_eol=eol).exists():
        return  Associacao.objects.filter(unidade__codigo_eol=eol).get()

    return None


def get_acao(nome):
    if Acao.objects.filter(nome=nome).exists():
        return Acao.objects.filter(nome=nome).get()

    return Acao.objects.create(nome=nome)


def get_tipo_conta(nome):
    if TipoConta.objects.filter(nome=nome).exists():
        return TipoConta.objects.filter(nome=nome).get()

    return TipoConta.objects.create(nome=nome)


def get_acao_associacao(acao, associacao):
    if AcaoAssociacao.objects.filter(acao=acao, associacao=associacao).exists():
        return AcaoAssociacao.objects.filter(acao=acao, associacao=associacao).get()

    return AcaoAssociacao.objects.create(acao=acao, associacao=associacao)


def get_conta_associacao(tipo_conta, associacao):
    if ContaAssociacao.objects.filter(tipo_conta=tipo_conta, associacao=associacao).exists():
        return ContaAssociacao.objects.filter(tipo_conta=tipo_conta, associacao=associacao).get()

    return ContaAssociacao.objects.create(tipo_conta=tipo_conta, associacao=associacao)


def get_datas_periodo(nome_arquivo):
    base_name = os.path.basename(nome_arquivo)
    start_str_date, end_str_date = base_name[:10], base_name[13:23]
    start = datetime.datetime.strptime(start_str_date, '%Y_%m_%d')
    end = datetime.datetime.strptime(end_str_date, '%Y_%m_%d')

    return (start, end)

def get_periodo(nome_arquivo):
    start, end = get_datas_periodo(nome_arquivo)

    if Periodo.objects.filter(data_inicio_realizacao_despesas=start, data_fim_realizacao_despesas=end).exists():
        return Periodo.objects.filter(data_inicio_realizacao_despesas=start, data_fim_realizacao_despesas=end).get()

    return Periodo.objects.create(
        data_inicio_realizacao_despesas=start,
        data_fim_realizacao_despesas=end
    )


def processa_repasse(reader, conta, nome_arquivo):
    for index, row in enumerate(reader):
        if index != 0:
            logger.info('Linha %s: %s', index, row)
            associacao = get_associacao(row[0])
            if not associacao:
                logger.info('Associação com código eol: %s', row[0])
            try:
                valor_capital = get_valor(row[1])
                valor_custeio = get_valor(row[2])
                valor_livre = get_valor(row[3])
                acao = get_acao(row[4])
                tipo_conta = get_tipo_conta(conta)
                acao_associacao = get_acao_associacao(acao, associacao)
                conta_associacao = get_conta_associacao(tipo_conta, associacao)
                periodo = get_periodo(nome_arquivo)

                if valor_capital > 0 or valor_custeio > 0 or valor_livre > 0:
                    Repasse.objects.create(
                        associacao=associacao,
                        valor_capital=valor_capital,
                        valor_custeio=valor_custeio,
                        valor_livre=valor_livre,
                        conta_associacao=conta_associacao,
                        acao_associacao=acao_associacao,
                        periodo=periodo,
                        status=StatusRepasse.PENDENTE.name
                    )
            except Exception as e:
                logger.info("Error %s", str(e))


def carrega_repasses_previstos(arquivo):
    logger.info("Processando arquivo %s", arquivo.identificador)
    tipo_conta = TipoContaEnum.CARTAO.value if 'cartao' in arquivo.identificador else TipoContaEnum.CHEQUE.value

    with open(arquivo.conteudo.path, 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        processa_repasse(reader, tipo_conta, arquivo.identificador)
