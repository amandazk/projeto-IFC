from rest_framework import generics, permissions

from demanda.models import TbDemanda
from demanda.serializers import DemandaSerializer

class DemandaList(generics.ListAPIView):
    """Listando demanda"""
    queryset = TbDemanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = ()

class DemandaDestroy(generics.DestroyAPIView):
    """Excluindo demanda"""
    queryset = TbDemanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class DemandaUpdate(generics.UpdateAPIView):
    """Update de demanda"""
    queryset = TbDemanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class DemandaCreate(generics.CreateAPIView):
    """Criando demanda"""
    queryset = TbDemanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class DemandaGet(generics.RetrieveAPIView):
    """Listando uma demanda"""
    queryset = TbDemanda.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = ()

