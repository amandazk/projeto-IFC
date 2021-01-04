from django.apps import AppConfig
from django.apps import apps

model = apps.get_model('pessoas', 'Pessoa')

class VoluntariadoConfig(AppConfig):
    name = 'voluntariado'
