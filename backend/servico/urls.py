from django.conf.urls import url

from .views import (
    ServicoList, ServicoDestroy, ServicoCreate, ServicoGet, ServicoUpdate
)

urlpatterns = [
    url(r'servico/$', ServicoList.as_view()),
    url(r'servico/(?P<pk>\d+)/$', ServicoDestroy.as_view()),
    url(r'servico/add/$', ServicoCreate.as_view()),
    url(r'servico/get/(?P<pk>\d+)/$', ServicoGet.as_view()),
    url(r'servico/edit/(?P<pk>\d+)/$', ServicoUpdate.as_view()),
]