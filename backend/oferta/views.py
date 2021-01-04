from rest_framework import generics, permissions

from oferta.models import Oferta
from oferta.serializers import OfertaSerializer

class OfertaList(generics.ListAPIView):
    """Listando oferta"""
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = ()

class OfertaDestroy(generics.DestroyAPIView):
    """Excluindo oferta"""
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class OfertaUpdate(generics.UpdateAPIView):
    """Update de oferta"""
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class OfertaCreate(generics.CreateAPIView):
    """Criando oferta"""
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class OfertaGet(generics.RetrieveAPIView):
    """Listando uma oferta"""
    queryset = Oferta.objects.all()
    serializer_class =OfertaSerializer
    permission_classes = ()

