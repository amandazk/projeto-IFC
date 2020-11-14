from rest_framework import serializers
from noticia.models import TbNoticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbNoticia
        fields = (
            '__all__')
