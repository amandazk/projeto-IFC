from django.contrib import admin
from voluntariado.models import TbVoluntariado

class Voluntariado(admin.ModelAdmin):
    list_display = ('voluntariado_id', 'desc_voluntariado')
    list_display_links = ('voluntariado_id', )
    list_per_page = 10

admin.site.register(TbVoluntariado, Voluntariado)
