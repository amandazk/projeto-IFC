from rest_framework import serializers
from campanhas.models import TbCampanha

class CampanhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCampanha
        fields = (
            '__all__')

