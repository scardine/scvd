from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from main.models import Indicador, Tema


class Index(TemplateView):
    template_name = 'index.html'


class IndicadorList(ListView):
    queryset = Indicador.objects.all()


class IndicadorDetail(DetailView):
    queryset = Indicador.objects.all()


class TemaList(ListView):
    queryset = Tema.objects.all()


class TemaDetail(DetailView):
    queryset = Tema.objects.all()
