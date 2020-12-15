"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('campanhas.urls')),
    path('api/', include('pessoas.urls')),
    path('api/', include('voluntariado.urls')),
    path('api/', include('demanda.urls')),
    path('api/', include('oferta.urls')),
    path('api/', include('servico.urls')),
    path('api/', include('noticia.urls')),
    path('api/auth/token/', TokenObtainPairView.as_view(), name="token"),
    #path('', include('index.urls'))
]
