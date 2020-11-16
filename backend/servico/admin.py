from django.contrib import admin

from django.contrib import admin
from servico.models import TbServico

class Servicos(admin.ModelAdmin):
    list_display = ('id_servico', 'titulo_servico', 'desc_servico')
    list_display_links = ('id_servico', 'titulo_servico')
    # search_fields = ('titulo_campanha',)
    list_per_page = 10

admin.site.register(TbServico, Servicos)