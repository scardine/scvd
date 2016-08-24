"""scvd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.Index.as_view(), name='home'),
    url(r'^tema/$', main_views.TemaList.as_view(), name='tema-list'),
    url(r'^tema/(?P<pk>\d+)/', main_views.TemaDetail.as_view(), name='tema-detail'),
    url(r'^indicadores/$', main_views.IndicadorList.as_view(), name='indicador-list'),
    url(r'^indicadores/(?P<pk>\d+)/', main_views.IndicadorDetail.as_view(), name='indicador-detail'),
]
