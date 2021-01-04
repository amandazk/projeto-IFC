from django.apps import AppConfig
from django.apps import apps

model = apps.get_model('pessoas', 'Pessoa')
model = apps.get_model('servico', 'Servico')

class DemandaConfig(AppConfig):
    name = 'demanda'
