from django.contrib import admin
from voluntariado.models import Voluntariado

class Voluntariados(admin.ModelAdmin):
    list_display = ('voluntariado_id', 'titulo_voluntariado')
    list_display_links = ('voluntariado_id', 'titulo_voluntariado')
    list_per_page = 10

admin.site.register(Voluntariado, Voluntariados)
