from rest_framework import serializers
from demanda.models import Demanda

class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = (
            '__all__')
