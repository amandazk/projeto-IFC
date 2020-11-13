from django.apps import AppConfig
from django.apps import apps

model = apps.get_model('pessoas', 'TbPessoa')
# model = apps.get_model('servico', 'Tbservico')

class DemandaConfig(AppConfig):
    name = 'demanda'
