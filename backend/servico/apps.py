from django.apps import AppConfig
from django.apps import apps

model = apps.get_model('oferta', 'TbOferta')
model = apps.get_model('demanda', 'TbDemanda')
model = apps.get_model('voluntariado', 'TbVoluntariado')

class ServicoConfig(AppConfig):
    name = 'servico'
