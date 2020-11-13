from django.conf.urls import url

from .views import (
    DemandaList, DemandaDestroy, DemandaCreate, DemandaGet, DemandaUpdate
)

urlpatterns = [
    url(r'demanda/$', DemandaList.as_view()),
    url(r'demanda/(?P<pk>\d+)/$', DemandaDestroy.as_view()),
    url(r'demanda/add/$', DemandaCreate.as_view()),
    url(r'demanda/get/(?P<pk>\d+)/$', DemandaGet.as_view()),
    url(r'demanda/edit/(?P<pk>\d+)/$', DemandaUpdate.as_view()),
]