from rest_framework import serializers
from campanhas.models import Campanha

class CampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campanha
        fields = (
            '__all__')

