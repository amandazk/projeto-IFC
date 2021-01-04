from rest_framework import generics, permissions

from campanhas.models import Campanha
from campanhas.serializers import CampanhaSerializer

class CampanhaList(generics.ListAPIView):
    """Listando campanhas"""
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    permission_classes = ()

class CampanhaDestroy(generics.DestroyAPIView):
    """Excluindo campanha"""
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class CampanhaUpdate(generics.UpdateAPIView):
    """Update de campanha"""
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class CampanhaCreate(generics.CreateAPIView):
    """Criando campanha"""
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class CampanhaGet(generics.RetrieveAPIView):
    """Listando uma campanha"""
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
    permission_classes = ()

