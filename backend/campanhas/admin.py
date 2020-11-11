from django.contrib import admin
from campanhas.models import TbCampanha

class Campanhas(admin.ModelAdmin):
    list_display = ('campanha_id', 'ativo', 'titulo_campanha', 'pessoa')
    list_display_links = ('campanha_id', 'titulo_campanha')
    search_fields = ('titulo_campanha',)
    list_per_page = 10

admin.site.register(TbCampanha, Campanhas)
