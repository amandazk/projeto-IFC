from django.conf.urls import url

from .views import (
    PessoaList, PessoaDestroy, PessoaUpdate, PessoaCreate, PessoaGet
)

urlpatterns = [
    url(r'pessoas/$', PessoaList.as_view()),
    url(r'pessoas/(?P<pk>\d+)/$', PessoaDestroy.as_view()),
    url(r'pessoas/add/$', PessoaCreate.as_view()),
    url(r'pessoas/get/(?P<pk>\d+)/$', PessoaGet.as_view()),
    url(r'pessoas/edit/(?P<pk>\d+)/$', PessoaUpdate.as_view()),
]