from rest_framework import serializers
from voluntariado.models import Voluntariado


class VoluntariadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntariado
        fields = (
            '__all__'
        )
