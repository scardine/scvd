from django.contrib import admin

from main.models import Fonte


class FonteAdmin(admin.ModelAdmin):
    search_fields = ('fonte_descricao',)

admin.site.register(Fonte, FonteAdmin)