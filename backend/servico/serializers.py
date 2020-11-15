from rest_framework import serializers
from servico.models import TbServico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbServico
        fields = (
            '__all__')
