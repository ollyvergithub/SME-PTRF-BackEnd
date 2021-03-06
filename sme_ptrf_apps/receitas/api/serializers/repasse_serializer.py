from rest_framework import serializers

from sme_ptrf_apps.core.api.serializers.acao_associacao_serializer import AcaoAssociacaoLookUpSerializer
from sme_ptrf_apps.core.api.serializers.conta_associacao_serializer import ContaAssociacaoLookUpSerializer
from sme_ptrf_apps.core.models import Periodo

from ...models import Repasse


class PeriodoSerializer(serializers.ModelSerializer):
    serializers.DateField(format="")
    class Meta:
        model = Periodo
        fields = [
            'uuid',
            'data_inicio_realizacao_despesas',
            'data_fim_realizacao_despesas'
        ]


class RepasseSerializer(serializers.ModelSerializer):
    valor_capital = serializers.SerializerMethodField('get_valor_capital')
    valor_custeio = serializers.SerializerMethodField('get_valor_custeio')
    valor_livre = serializers.SerializerMethodField('get_valor_livre')
    acao_associacao = AcaoAssociacaoLookUpSerializer()
    conta_associacao = ContaAssociacaoLookUpSerializer()
    periodo = PeriodoSerializer()

    def get_valor_capital(self, obj):
        """Quando o repasse tiver a receita do tipo capital realizado é retornado zero."""
        return '0.00' if obj.realizado_capital else str(obj.valor_capital)

    def get_valor_custeio(self, obj):
        """Quando o repasse tiver a receita do tipo custeio realizado é retornado zero."""
        return '0.00' if obj.realizado_custeio else str(obj.valor_custeio)

    def get_valor_livre(self, obj):
        """Quando o repasse tiver a receita do tipo livre realizado é retornado zero."""
        return '0.00' if obj.realizado_livre else str(obj.valor_livre)

    class Meta:
        model = Repasse
        fields = [
            'uuid',
            'valor_capital',
            'valor_custeio',
            'valor_livre',
            'acao_associacao',
            'conta_associacao',
            'periodo']
