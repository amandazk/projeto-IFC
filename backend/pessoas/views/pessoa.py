from rest_framework import generics, permissions

from pessoas.models import Pessoa
from pessoas.serializers import PessoaSerializer

class PessoaList(generics.ListAPIView):
    """Listando todas as pessoas"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()


class PessoaDestroy(generics.DestroyAPIView):
    """Excluindo pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()


class PessoaUpdate(generics.UpdateAPIView):
    """Update de pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()

class PessoaCreate(generics.CreateAPIView):
    """Criando pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()



class PessoaGet(generics.RetrieveAPIView):
    """Listando uma pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()