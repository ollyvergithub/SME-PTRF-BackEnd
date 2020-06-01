from django.db import models
from sme_ptrf_apps.core.models_abstracts import ModeloBase


class RelacaoBens(ModeloBase):
    conta_associacao = models.ForeignKey('ContaAssociacao', on_delete=models.PROTECT,
                                         related_name='relacoes_de_bens', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Relação de bens'
        verbose_name_plural = 'Relações de bens'

    def __str__(self):
        return f"Documento gerado dia {self.criado_em.strftime('%d/%m/%Y %H:%S')}"
