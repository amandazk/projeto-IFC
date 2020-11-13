from rest_framework import serializers
from voluntariado.models import TbVoluntariado


class VoluntariadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbVoluntariado
        fields = (
            '__all__'
        )
