from rest_framework import generics, permissions

from noticia.models import Noticia
from noticia.serializers import NoticiaSerializer

class NoticiaList(generics.ListAPIView):
    """Listando noticia"""
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = ()

class NoticiaDestroy(generics.DestroyAPIView):
    """Excluindo noticia"""
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class NoticiaUpdate(generics.UpdateAPIView):
    """Update de noticia"""
    queryset = Noticia.objects.all()
    serializer_class =NoticiaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class NoticiaCreate(generics.CreateAPIView):
    """Criando noticia"""
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class NoticiaGet(generics.RetrieveAPIView):
    """Listando uma noticia"""
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = ()

