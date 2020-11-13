from django.conf.urls import url

from .views import (
    VoluntariadoList, VoluntariadoDestroy, VoluntariadoCreate, VoluntariadoGet, VoluntariadoUpdate
)

urlpatterns = [
    url(r'voluntariado/$', VoluntariadoList.as_view()),
    url(r'voluntariado/(?P<pk>\d+)/$', VoluntariadoDestroy.as_view()),
    url(r'voluntariado/add/$', VoluntariadoCreate.as_view()),
    url(r'voluntariado/get/(?P<pk>\d+)/$', VoluntariadoGet.as_view()),
    url(r'voluntariado/edit/(?P<pk>\d+)/$', VoluntariadoUpdate.as_view()),
]