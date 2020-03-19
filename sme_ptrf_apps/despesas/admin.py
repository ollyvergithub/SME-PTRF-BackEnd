from django.contrib import admin

from .models import TipoTransacao, TipoDocumento, TipoCusteio, TipoAplicacaoRecurso, EspecificacaoMaterialServico, \
    Despesa

admin.site.register(TipoTransacao)
admin.site.register(TipoDocumento)
admin.site.register(TipoCusteio)
admin.site.register(TipoAplicacaoRecurso)
admin.site.register(EspecificacaoMaterialServico)
admin.site.register(Despesa)
