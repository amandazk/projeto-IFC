from rest_framework import serializers
from oferta.models import TbOferta

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbOferta
        fields = (
            '__all__')
