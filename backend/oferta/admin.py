from django.contrib import admin
from oferta.models import TbOferta

class Oferta(admin.ModelAdmin):
    list_display = ('oferta_id', 'titulo_oferta')
    list_display_links = ('oferta_id', 'titulo_oferta')
    search_fields = ('titulo_oferta',)
    list_per_page = 10

admin.site.register(TbOferta, Oferta)
