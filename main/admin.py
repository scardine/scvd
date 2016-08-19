from django.contrib import admin

from main.models import Fonte, Grupo, Indicador


class FonteAdmin(admin.ModelAdmin):
    search_fields = ('fonte_descricao',)


class IndicadorAdmin(admin.ModelAdmin):
    search_fields = ('indicador_nome', 'indicador_descricao',)
    list_display = ('indicador_nome', 'indicador_periodo')
    list_filter = ('indicador_formato', 'temas')


admin.site.register(Fonte, FonteAdmin)
admin.site.register(Grupo)
admin.site.register(Indicador, IndicadorAdmin)
