from django.contrib import admin

from main.models import Fonte, Grupo, Indicador, Localidade, Mapa, Tema, TipoLoc, Uf, Unidade


class FonteAdmin(admin.ModelAdmin):
    search_fields = ('fonte_descricao',)


class IndicadorAdmin(admin.ModelAdmin):
    search_fields = ('indicador_nome', 'indicador_descricao',)
    list_display = ('indicador_nome', 'indicador_periodo')
    list_filter = ('indicador_formato', 'temas')


class LocalidadeAdmin(admin.ModelAdmin):
    list_filter = ('tipoloc',)
    search_fields = ('localidade_descricao',)


class TemaAdmin(admin.ModelAdmin):
    list_display = ('tema_descricao', 'tema_ordem',)
    list_editable = ('tema_ordem',)


class UFAdmin(admin.ModelAdmin):
    list_display = ('uf_sigla', 'uf_nome',)


admin.site.register(Fonte, FonteAdmin)
admin.site.register(Grupo)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(Localidade, LocalidadeAdmin)
admin.site.register(Mapa)
admin.site.register(Tema, TemaAdmin)
admin.site.register(TipoLoc)
admin.site.register(Uf, UFAdmin)
admin.site.register(Unidade)

