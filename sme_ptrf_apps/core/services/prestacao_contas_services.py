import logging

from django.db import transaction

from ..models import PrestacaoConta, AcaoAssociacao, FechamentoPeriodo, ContaAssociacao
from ..services import info_acoes_associacao_no_periodo
from ..services.demonstrativo_financeiro import gerar_arquivo_demonstrativo_financeiro
from ..services.relacao_bens import gerar_arquivo_relacao_de_bens
from ...despesas.models import RateioDespesa
from ...receitas.models import Receita

logger = logging.getLogger(__name__)


@transaction.atomic
def concluir_prestacao_de_contas(periodo, associacao):
    prestacao = PrestacaoConta.abrir(periodo=periodo, associacao=associacao)
    logger.info(f'Aberta a prestação de contas {prestacao}.')

    associacao = prestacao.associacao
    periodo = prestacao.periodo
    acoes = associacao.acoes.filter(status=AcaoAssociacao.STATUS_ATIVA)
    contas = associacao.contas.filter(status=ContaAssociacao.STATUS_ATIVA)

    _criar_fechamentos(acoes, contas, periodo, prestacao)
    logger.info(f'Fechamentos criados para a prestação de contas {prestacao}.')

    _criar_documentos(acoes, contas, periodo, prestacao)
    logger.info(f'Documentos gerados para a prestação de contas {prestacao}.')

    prestacao = prestacao.concluir()
    logger.info(f'Concluída a prestação de contas {prestacao}.')

    return prestacao


def _criar_fechamentos(acoes, contas, periodo, prestacao):
    logger.info(f'Criando fechamentos do período {periodo} e prestacao {prestacao}...')
    for conta in contas:
        logger.info(f'Criando fechamentos da conta {conta}.')
        for acao in acoes:
            logger.info(f'Criando fechamentos da ação {acao}.')
            totais_receitas = Receita.totais_por_acao_associacao_no_periodo(acao_associacao=acao, periodo=periodo,
                                                                            conta=conta)
            totais_despesas = RateioDespesa.totais_por_acao_associacao_no_periodo(acao_associacao=acao, periodo=periodo,
                                                                                  conta=conta)
            especificacoes_despesas = RateioDespesa.especificacoes_dos_rateios_da_acao_associacao_no_periodo(
                acao_associacao=acao, periodo=periodo)
            FechamentoPeriodo.criar(
                prestacao_conta=prestacao,
                acao_associacao=acao,
                conta_associacao=conta,
                total_receitas_capital=totais_receitas['total_receitas_capital'],
                total_receitas_devolucao_capital=totais_receitas['total_receitas_devolucao_capital'],
                total_repasses_capital=totais_receitas['total_repasses_capital'],
                total_receitas_custeio=totais_receitas['total_receitas_custeio'],
                total_receitas_devolucao_custeio=totais_receitas['total_receitas_devolucao_custeio'],
                total_receitas_devolucao_livre=totais_receitas['total_receitas_devolucao_livre'],
                total_repasses_custeio=totais_receitas['total_repasses_custeio'],
                total_despesas_capital=totais_despesas['total_despesas_capital'],
                total_despesas_custeio=totais_despesas['total_despesas_custeio'],
                total_receitas_livre=totais_receitas['total_receitas_livre'],
                total_repasses_livre=totais_receitas['total_repasses_livre'],
                total_receitas_nao_conciliadas_capital=totais_receitas['total_receitas_nao_conciliadas_capital'],
                total_receitas_nao_conciliadas_custeio=totais_receitas['total_receitas_nao_conciliadas_custeio'],
                total_receitas_nao_conciliadas_livre=totais_receitas['total_receitas_nao_conciliadas_livre'],
                total_despesas_nao_conciliadas_capital=totais_despesas['total_despesas_nao_conciliadas_capital'],
                total_despesas_nao_conciliadas_custeio=totais_despesas['total_despesas_nao_conciliadas_custeio'],
                especificacoes_despesas=especificacoes_despesas
            )


def _criar_documentos(acoes, contas, periodo, prestacao):
    logger.info(f'Criando documentos do período {periodo} e prestacao {prestacao}...')
    for conta in contas:
        logger.info(f'Gerando relação de bens da conta {conta}.')
        gerar_arquivo_relacao_de_bens(periodo=periodo, conta_associacao=conta, prestacao=prestacao)
        for acao in acoes:
            logger.info(f'Gerando demonstrativo financeiro da ação {acao} e conta {conta}.')
            gerar_arquivo_demonstrativo_financeiro(periodo=periodo, conta_associacao=conta, acao_associacao=acao,
                                                   prestacao=prestacao)


def reabrir_prestacao_de_contas(prestacao_contas_uuid):
    logger.info(f'Reabrindo a prestação de contas de uuid {prestacao_contas_uuid}.')
    concluido = PrestacaoConta.reabrir(uuid=prestacao_contas_uuid)
    if concluido:
        logger.info(f'Prestação de contas de uuid {prestacao_contas_uuid} foi reaberta. Seus registros foram apagados.')
    return concluido

def devolver_prestacao_de_contas(prestacao_contas_uuid):
    logger.info(f'Devolvendo a prestação de contas de uuid {prestacao_contas_uuid}.')
    prestacao = PrestacaoConta.devolver(uuid=prestacao_contas_uuid)
    return prestacao



def informacoes_financeiras_para_atas(prestacao_contas):
    def totaliza_info_acoes(info_acoes):
        totalizador = {
            'saldo_reprogramado': 0,
            'saldo_reprogramado_capital': 0,
            'saldo_reprogramado_custeio': 0,
            'saldo_reprogramado_livre': 0,

            'receitas_no_periodo': 0,

            'receitas_devolucao_no_periodo': 0,
            'receitas_devolucao_no_periodo_custeio': 0,
            'receitas_devolucao_no_periodo_capital': 0,
            'receitas_devolucao_no_periodo_livre': 0,

            'repasses_no_periodo': 0,
            'repasses_no_periodo_capital': 0,
            'repasses_no_periodo_custeio': 0,
            'repasses_no_periodo_livre': 0,

            'outras_receitas_no_periodo': 0,
            'outras_receitas_no_periodo_capital': 0,
            'outras_receitas_no_periodo_custeio': 0,
            'outras_receitas_no_periodo_livre': 0,

            'despesas_no_periodo': 0,
            'despesas_no_periodo_capital': 0,
            'despesas_no_periodo_custeio': 0,

            'despesas_nao_conciliadas': 0,
            'despesas_nao_conciliadas_capital': 0,
            'despesas_nao_conciliadas_custeio': 0,

            'receitas_nao_conciliadas': 0,
            'receitas_nao_conciliadas_capital': 0,
            'receitas_nao_conciliadas_custeio': 0,
            'receitas_nao_conciliadas_livre': 0,

            'saldo_atual_custeio': 0,
            'saldo_atual_capital': 0,
            'saldo_atual_livre': 0,
            'saldo_atual_total': 0,

            'repasses_nao_realizados_capital': 0,
            'repasses_nao_realizados_custeio': 0,
            'repasses_nao_realizados_livre': 0
        }
        for info_acao in info_acoes:
            for key in totalizador.keys():
                totalizador[key] += info_acao[key]

        return totalizador

    logger.info(
        f'Get info financeiras para ata. Associacao:{prestacao_contas.associacao.uuid} Período:{prestacao_contas.periodo}')

    info_contas = []
    for conta_associacao in prestacao_contas.associacao.contas.all():
        logger.info(
            f'Get info financeiras por conta para a ata. Associacao:{prestacao_contas.associacao.uuid} Conta:{conta_associacao}')
        info_acoes = info_acoes_associacao_no_periodo(associacao_uuid=prestacao_contas.associacao.uuid,
                                                      periodo=prestacao_contas.periodo,
                                                      conta=conta_associacao)

        info_acoes = [info for info in info_acoes if
                      info['saldo_reprogramado'] or info['receitas_no_periodo'] or info['despesas_no_periodo']]

        info_contas.append(
            {
                'conta_associacao': {
                    'uuid': f'{conta_associacao.uuid}',
                    'nome': f'{conta_associacao.tipo_conta.nome}',
                    'banco_nome': f'{conta_associacao.banco_nome}',
                    'agencia': f'{conta_associacao.agencia}',
                    'numero_conta': f'{conta_associacao.numero_conta}',
                },
                'acoes': info_acoes,
                'totais': totaliza_info_acoes(info_acoes),
            }
        )

    info = {
        'uuid': prestacao_contas.uuid,
        'contas': info_contas,
    }

    return info
