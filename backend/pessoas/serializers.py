from rest_framework import serializers
from pessoas.models import TbPessoa
from pessoas.validators import cpf_valido

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbPessoa
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf_pessoa']):
            raise serializers.ValidationError({'cpf_pessoa': "O CPF deve ser válido"})
        return data