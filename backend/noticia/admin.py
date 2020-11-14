from django.contrib import admin
from noticia.models import TbNoticia

class Noticia(admin.ModelAdmin):
    list_display = ('noticia_id', 'titulo_noticia')
    list_display_links = ('noticia_id', 'titulo_noticia')
    search_fields = ('titulo_noticia',)
    list_per_page = 10

admin.site.register(TbNoticia, Noticia)

