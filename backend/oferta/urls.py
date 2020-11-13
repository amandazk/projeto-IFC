from django.conf.urls import url

from .views import (
    OfertaList, OfertaDestroy, OfertaCreate, OfertaGet, OfertaUpdate
)

urlpatterns = [
    url(r'oferta/$', OfertaList.as_view()),
    url(r'oferta/(?P<pk>\d+)/$', OfertaDestroy.as_view()),
    url(r'oferta/add/$', OfertaCreate.as_view()),
    url(r'oferta/get/(?P<pk>\d+)/$', OfertaGet.as_view()),
    url(r'oferta/edit/(?P<pk>\d+)/$', OfertaUpdate.as_view()),
]