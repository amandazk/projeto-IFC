from rest_framework import generics, permissions

from oferta.models import TbOferta
from oferta.serializers import OfertaSerializer

class OfertaList(generics.ListAPIView):
    """Listando oferta"""
    queryset = TbOferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = ()

class OfertaDestroy(generics.DestroyAPIView):
    """Excluindo oferta"""
    queryset = TbOferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class OfertaUpdate(generics.UpdateAPIView):
    """Update de oferta"""
    queryset = TbOferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class OfertaCreate(generics.CreateAPIView):
    """Criando oferta"""
    queryset = TbOferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class OfertaGet(generics.RetrieveAPIView):
    """Listando uma oferta"""
    queryset = TbOferta.objects.all()
    serializer_class =OfertaSerializer
    permission_classes = ()

