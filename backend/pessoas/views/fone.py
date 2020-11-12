from rest_framework import generics, permissions

from pessoas.models import TbFone
from pessoas.serializers import FoneSerializer

class FoneList(generics.ListAPIView):
    """Listando todos os fones"""
    queryset = TbFone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = ()


class FoneDestroy(generics.DestroyAPIView):
    """Excluindo fone"""
    queryset = TbFone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )


class FoneUpdate(generics.UpdateAPIView):
    """Update de fone"""
    queryset = TbFone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class FoneCreate(generics.CreateAPIView):
    """Criando fone"""
    queryset = TbFone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )


class FoneGet(generics.RetrieveAPIView):
    """Listando um fone"""
    queryset = TbFone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = ()