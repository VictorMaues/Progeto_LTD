from rest_framework import serializers
from .models import Paciente, Exame

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    exames = ExameSerializer(many=True, read_only=True)
    
    class Meta:
        model = Paciente
        fields = '__all__'
