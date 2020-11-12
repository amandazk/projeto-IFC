from django.conf.urls import url

from pessoas.views import (
    PessoaList, PessoaDestroy, PessoaUpdate, PessoaCreate, PessoaGet,
    FoneList, FoneDestroy, FoneUpdate, FoneCreate, FoneGet

)





urlpatterns = [
    url(r'pessoas/$', PessoaList.as_view()),
    url(r'pessoas/(?P<pk>\d+)/$', PessoaDestroy.as_view()),
    url(r'pessoas/add/$', PessoaCreate.as_view()),
    url(r'pessoas/get/(?P<pk>\d+)/$', PessoaGet.as_view()),
    url(r'pessoas/edit/(?P<pk>\d+)/$', PessoaUpdate.as_view()),
   
    url(r'fones/$', FoneList.as_view()),
    url(r'fones/(?P<pk>\d+)/$', FoneDestroy.as_view()),
    url(r'fones/add/$', FoneCreate.as_view()),
    url(r'fones/get/(?P<pk>\d+)/$', FoneGet.as_view()),
    url(r'fone/edit/(?P<pk>\d+)/$', FoneUpdate.as_view()),
]