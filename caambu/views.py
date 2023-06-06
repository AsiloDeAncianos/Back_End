from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BenefactorSerializer, InstitucionAsiloSerializer, CampaniaSerializer, DonacionSerializer, GestorSerializer, RecojosProgramadosSerializer
from .models import Benefactor, InstitucionAsilo, Campania, Donacion, Gestor, RecojosProgramados

# Create your views here.

class BenefactorView(viewsets.ModelViewSet):
    serializer_class = BenefactorSerializer
    queryset = Benefactor.objects.all()

class InstitucionAsiloView(viewsets.ModelViewSet):
    serializer_class = InstitucionAsiloSerializer
    queryset = InstitucionAsilo.objects.all()

class CampaniaView(viewsets.ModelViewSet):
    serializer_class = CampaniaSerializer
    queryset = Campania.objects.all()

class DonacionView(viewsets.ModelViewSet):
    serializer_class = DonacionSerializer
    queryset = Donacion.objects.all()

class GestorView(viewsets.ModelViewSet):
    serializer_class = GestorSerializer
    queryset = Gestor.objects.all()

class RecojosProgramadosView(viewsets.ModelViewSet):
    serializer_class = RecojosProgramadosSerializer
    queryset = RecojosProgramados.objects.all()
    