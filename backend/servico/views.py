from rest_framework import generics, permissions

from servico.models import Servico
from servico.serializers import ServicoSerializer

class ServicoList(generics.ListAPIView):
    """Listando servico"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = ()

class ServicoDestroy(generics.DestroyAPIView):
    """Excluindo servico"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class ServicoUpdate(generics.UpdateAPIView):
    """Update de Servico"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class ServicoCreate(generics.CreateAPIView):
    """Criando Servico"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class ServicoGet(generics.RetrieveAPIView):
    """Listando uma Servico"""
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = ()

