from rest_framework import serializers
from noticia.models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = (
            '__all__')
