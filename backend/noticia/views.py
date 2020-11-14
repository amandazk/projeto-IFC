from rest_framework import generics, permissions

from noticia.models import TbNoticia
from noticia.serializers import NoticiaSerializer

class NoticiaList(generics.ListAPIView):
    """Listando noticia"""
    queryset = TbNoticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = ()

class NoticiaDestroy(generics.DestroyAPIView):
    """Excluindo noticia"""
    queryset = TbNoticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class NoticiaUpdate(generics.UpdateAPIView):
    """Update de noticia"""
    queryset = TbNoticia.objects.all()
    serializer_class =NoticiaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class NoticiaCreate(generics.CreateAPIView):
    """Criando noticia"""
    queryset = TbNoticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class NoticiaGet(generics.RetrieveAPIView):
    """Listando uma noticia"""
    queryset = TbNoticia.objects.all()
    serializer_class = NoticiaSerializer
    permission_classes = ()

