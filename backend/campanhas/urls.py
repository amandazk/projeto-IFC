from django.conf.urls import url

from .views import (
    CampanhaList, CampanhaDestroy, CampanhaCreate, CampanhaGet, CampanhaUpdate
)

urlpatterns = [
    url(r'campanhas/$', CampanhaList.as_view()),
    url(r'campanhas/(?P<pk>\d+)/$', CampanhaDestroy.as_view()),
    url(r'campanhas/add/$', CampanhaCreate.as_view()),
    url(r'campanhas/get/(?P<pk>\d+)/$', CampanhaGet.as_view()),
    url(r'campanhas/edit/(?P<pk>\d+)/$', CampanhaUpdate.as_view()),
]