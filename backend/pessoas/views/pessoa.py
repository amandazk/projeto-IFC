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
    permission_classes = (
        permissions.IsAdminUser,
    )


class PessoaUpdate(generics.UpdateAPIView):
    """Update de pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class PessoaCreate(generics.CreateAPIView):
    """Criando pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )


class PessoaGet(generics.RetrieveAPIView):
    """Listando uma pessoa"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()