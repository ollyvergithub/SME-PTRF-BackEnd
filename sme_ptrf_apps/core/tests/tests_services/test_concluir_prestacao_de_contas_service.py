import pytest

from ...models.prestacao_conta import STATUS_ABERTO
from ...services import concluir_prestacao_de_contas

pytestmark = pytest.mark.django_db


def test_prestacao_de_contas_deve_ser_atualizada(prestacao_conta_iniciada):
    observacoes = "Teste"
    prestacao = concluir_prestacao_de_contas(prestacao_contas_uuid=prestacao_conta_iniciada.uuid,
                                             observacoes=observacoes)

    assert prestacao.observacoes == observacoes, "Deveria ter gravado as observações"
    assert prestacao.status == STATUS_ABERTO, "O status deveria continuar como aberto."
    assert prestacao.conciliado, "Deveria ter sido marcada como conciliado."
    assert prestacao.conciliado_em is not None, "Deveria ter gravado a data e hora da última conciliação."


def test_fechamentos_devem_ser_criados_por_acao(prestacao_conta_iniciada,
                                                periodo_2020_1,
                                                receita_2020_1_role_repasse_custeio_conferida,
                                                receita_2020_1_ptrf_repasse_capital_conferida,
                                                receita_2020_1_role_repasse_capital_nao_conferida,
                                                receita_2019_2_role_repasse_capital_conferida,
                                                receita_2020_1_role_repasse_capital_conferida,
                                                receita_2020_1_role_rendimento_custeio_conferida,
                                                despesa_2020_1,
                                                rateio_despesa_2020_role_custeio_conferido,
                                                rateio_despesa_2020_role_custeio_nao_conferido,
                                                rateio_despesa_2020_role_capital_conferido,
                                                despesa_2019_2,
                                                rateio_despesa_2019_role_conferido):
    observacoes = "Teste"
    prestacao = concluir_prestacao_de_contas(prestacao_contas_uuid=prestacao_conta_iniciada.uuid,
                                             observacoes=observacoes)
    assert prestacao.fechamentos_da_prestacao.count() == 2, "Deveriam ter sido criados dois fechamentos, um por ação."


def test_deve_sumarizar_transacoes_incluindo_nao_conferidas(prestacao_conta_iniciada,
                                                            periodo_2020_1,
                                                            receita_2020_1_role_repasse_custeio_conferida,
                                                            receita_2020_1_role_repasse_capital_nao_conferida,
                                                            receita_2019_2_role_repasse_capital_conferida,
                                                            receita_2020_1_role_repasse_capital_conferida,
                                                            receita_2020_1_role_rendimento_custeio_conferida,
                                                            despesa_2020_1,
                                                            rateio_despesa_2020_role_custeio_conferido,
                                                            rateio_despesa_2020_role_custeio_nao_conferido,
                                                            rateio_despesa_2020_role_capital_conferido,
                                                            despesa_2019_2,
                                                            rateio_despesa_2019_role_conferido,
                                                            ):
    observacoes = "Teste"
    prestacao = concluir_prestacao_de_contas(prestacao_contas_uuid=prestacao_conta_iniciada.uuid,
                                             observacoes=observacoes)
    assert prestacao.fechamentos_da_prestacao.count() == 1, "Deveriam ter sido criado apenas um fechamento."

    fechamento = prestacao.fechamentos_da_prestacao.first()

    total_receitas_capital_esperado = receita_2020_1_role_repasse_capital_conferida.valor + \
                                      receita_2020_1_role_repasse_capital_nao_conferida.valor
    assert fechamento.total_receitas_capital == total_receitas_capital_esperado

    total_repasses_capital_esperado = receita_2020_1_role_repasse_capital_conferida.valor + \
                                      receita_2020_1_role_repasse_capital_nao_conferida.valor
    assert fechamento.total_repasses_capital == total_repasses_capital_esperado

    total_receitas_custeio_esperado = receita_2020_1_role_rendimento_custeio_conferida.valor + \
                                      receita_2020_1_role_repasse_custeio_conferida.valor
    assert fechamento.total_receitas_custeio == total_receitas_custeio_esperado

    total_repasses_custeio_esperado = receita_2020_1_role_repasse_custeio_conferida.valor
    assert fechamento.total_repasses_custeio == total_repasses_custeio_esperado

    total_despesas_capital = rateio_despesa_2020_role_capital_conferido.valor_rateio
    assert fechamento.total_despesas_capital == total_despesas_capital

    total_despesas_custeio = rateio_despesa_2020_role_custeio_conferido.valor_rateio + \
                             rateio_despesa_2020_role_custeio_nao_conferido.valor_rateio
    assert fechamento.total_despesas_custeio == total_despesas_custeio


def test_fechamentos_devem_ser_vinculados_a_anteriores(fechamento_periodo_2019_2,
                                                       prestacao_conta_2020_1_iniciada,
                                                       periodo_2019_2,
                                                       periodo_2020_1,
                                                       receita_2020_1_role_repasse_custeio_conferida,
                                                       receita_2020_1_role_repasse_capital_nao_conferida,
                                                       receita_2019_2_role_repasse_capital_conferida,
                                                       receita_2020_1_role_repasse_capital_conferida,
                                                       receita_2020_1_role_rendimento_custeio_conferida,
                                                       despesa_2020_1,
                                                       rateio_despesa_2020_role_custeio_conferido,
                                                       rateio_despesa_2020_role_custeio_nao_conferido,
                                                       rateio_despesa_2020_role_capital_conferido,
                                                       despesa_2019_2,
                                                       rateio_despesa_2019_role_conferido):
    observacoes = "Teste"
    prestacao = concluir_prestacao_de_contas(prestacao_contas_uuid=prestacao_conta_2020_1_iniciada.uuid,
                                             observacoes=observacoes)

    fechamento = prestacao.fechamentos_da_prestacao.first()

    assert fechamento.fechamento_anterior == fechamento_periodo_2019_2, "Deveria apontar para o fechamento anterior."