from django.apps import AppConfig
from django.apps import apps

model = apps.get_model('oferta', 'Oferta')
model = apps.get_model('demanda', 'Demanda')
model = apps.get_model('voluntariado', 'Voluntariado')

class ServicoConfig(AppConfig):
    name = 'servico'
