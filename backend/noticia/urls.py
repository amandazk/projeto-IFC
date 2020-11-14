from django.conf.urls import url

from .views import (
    NoticiaList, NoticiaDestroy, NoticiaCreate, NoticiaGet, NoticiaUpdate
)

urlpatterns = [
    url(r'noticia/$', NoticiaList.as_view()),
    url(r'noticia/(?P<pk>\d+)/$', NoticiaDestroy.as_view()),
    url(r'noticia/add/$', NoticiaCreate.as_view()),
    url(r'noticia/get/(?P<pk>\d+)/$', NoticiaGet.as_view()),
    url(r'noticia/edit/(?P<pk>\d+)/$', NoticiaUpdate.as_view()),
]