from rest_framework import serializers

from .models import Benefactor, InstitucionAsilo, Campania, Donacion, Gestor, RecojosProgramados

class BenefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = '__all__'

class InstitucionAsiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitucionAsilo
        fields = '__all__'

class CampaniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campania
        fields = '__all__'

class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = '__all__'

class GestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = '__all__'

class RecojosProgramadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecojosProgramados
        fields = '__all__'
        
