from rest_framework import serializers

from ...api.serializers.unidade_serializer import (UnidadeInfoAtaSerializer, UnidadeLookUpSerializer,
                                                   UnidadeListSerializer, UnidadeSerializer, UnidadeCreateSerializer)
from ...api.serializers.periodo_serializer import PeriodoLookUpSerializer
from ...models import Associacao, Unidade, Periodo


class AssociacaoSerializer(serializers.ModelSerializer):
    unidade = UnidadeLookUpSerializer(many=False)

    class Meta:
        model = Associacao
        fields = (
            'uuid',
            'ccm',
            'cnpj',
            'email',
            'nome',
            'status_regularidade',
            'unidade',
            'id',
            'processo_regularidade',
        )


class AssociacaoLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associacao
        fields = ('id', 'nome')


class AssociacaoCreateSerializer(serializers.ModelSerializer):
    unidade = UnidadeCreateSerializer(many=False)
    periodo_inicial = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        queryset=Periodo.objects.all(),
        allow_null=True,
        allow_empty=True,
    )

    class Meta:
        model = Associacao
        fields = '__all__'

    def create(self, validated_data):
        unidade = validated_data.pop('unidade')

        associacao = Associacao.objects.create(**validated_data)
        unidade_object = UnidadeCreateSerializer().create(unidade)
        associacao.unidade = unidade_object
        associacao.save()

        return associacao


class AssociacaoUpdateSerializer(serializers.ModelSerializer):
    unidade = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        queryset=Unidade.objects.all()
    )
    periodo_inicial = serializers.SlugRelatedField(
        slug_field='uuid',
        required=False,
        queryset=Periodo.objects.all(),
        allow_null=True,
        allow_empty=True,
    )

    class Meta:
        model = Associacao
        fields = '__all__'


class AssociacaoInfoAtaSerializer(serializers.ModelSerializer):
    unidade = UnidadeInfoAtaSerializer(many=False)

    class Meta:
        model = Associacao
        fields = [
            'uuid',
            'nome',
            'cnpj',
            'unidade',
        ]


class AssociacaoListSerializer(serializers.ModelSerializer):
    unidade = UnidadeListSerializer(many=False)

    class Meta:
        model = Associacao
        fields = [
            'uuid',
            'nome',
            'cnpj',
            'unidade',
            'status_regularidade',
            'motivo_nao_regularidade'
        ]


class AssociacaoCompletoSerializer(serializers.ModelSerializer):
    unidade = UnidadeSerializer(many=False)
    periodo_inicial = PeriodoLookUpSerializer()

    class Meta:
        model = Associacao
        fields = [
            'uuid',
            'nome',
            'unidade',
            'status_regularidade',
            'cnpj',
            'ccm',
            'email',
            'presidente_associacao',
            'presidente_conselho_fiscal',
            'processo_regularidade',
            'motivo_nao_regularidade',
            'periodo_inicial',
            'id'
        ]
