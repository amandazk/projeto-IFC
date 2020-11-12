from rest_framework import generics, permissions

from pessoas.models import TbPessoa
from pessoas.serializers import PessoaSerializer

class PessoaList(generics.ListAPIView):
    """Listando todas as pessoas"""
    queryset = TbPessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()


class PessoaDestroy(generics.DestroyAPIView):
    """Excluindo pessoa"""
    queryset = TbPessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )


class PessoaUpdate(generics.UpdateAPIView):
    """Update de pessoa"""
    queryset = TbPessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class PessoaCreate(generics.CreateAPIView):
    """Criando pessoa"""
    queryset = TbPessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )


class PessoaGet(generics.RetrieveAPIView):
    """Listando uma pessoa"""
    queryset = TbPessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = ()