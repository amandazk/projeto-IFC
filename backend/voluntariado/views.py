from rest_framework import generics, permissions

from voluntariado.models import Voluntariado
from voluntariado.serializers import VoluntariadoSerializer

class VoluntariadoList(generics.ListAPIView):
    """Listando voluntarios"""
    queryset = Voluntariado.objects.all()
    serializer_class = VoluntariadoSerializer
    permission_classes = ()

class VoluntariadoDestroy(generics.DestroyAPIView):
    """Excluindo voluntariado"""
    queryset = Voluntariado.objects.all()
    serializer_class = VoluntariadoSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class VoluntariadoUpdate(generics.UpdateAPIView):
    """Update de voluntariado"""
    queryset = Voluntariado.objects.all()
    serializer_class = VoluntariadoSerializer
    permission_classes = (
        permissions.IsAuthenticated, 
    )

class VoluntariadoCreate(generics.CreateAPIView):
    """Criando voluntariado"""
    queryset = Voluntariado.objects.all()
    serializer_class = VoluntariadoSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class VoluntariadoGet(generics.RetrieveAPIView):
    """Listando um voluntariado"""
    queryset = Voluntariado.objects.all()
    serializer_class = VoluntariadoSerializer
    permission_classes = ()
