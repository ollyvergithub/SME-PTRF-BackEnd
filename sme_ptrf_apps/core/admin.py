from django.contrib import admin

from .models import TipoConta, Acao, Associacao, ContaAssociacao

admin.site.register(TipoConta)
admin.site.register(Acao)
admin.site.register(Associacao)
admin.site.register(ContaAssociacao)
