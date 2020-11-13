from rest_framework import serializers
from demanda.models import TbDemanda

class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDemanda
        fields = (
            '__all__')
