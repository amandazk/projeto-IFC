from django.contrib import admin
from demanda.models import TbDemanda

class Demanda(admin.ModelAdmin):
    list_display = ('demanda_id', 'titulo_demanda')
    list_display_links = ('demanda_id', 'titulo_demanda')
    search_fields = ('titulo_demanda',)
    list_per_page = 10

admin.site.register(TbDemanda, Demanda)
