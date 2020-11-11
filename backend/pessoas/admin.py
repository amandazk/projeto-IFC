from django.contrib import admin
from pessoas.models import TbPessoa

class Pessoas(admin.ModelAdmin):
    list_display = ('pessoa_id','cpf_pessoa', 'nome_pessoa')
    list_display_links = ('cpf_pessoa', 'nome_pessoa')
    search_fields = ('cpf_pessoa', 'nome_pessoa')
    list_per_page = 10

admin.site.register(TbPessoa, Pessoas)