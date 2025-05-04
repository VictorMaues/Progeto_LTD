from rest_framework import viewsets, filters
from django.shortcuts import render
from django.db.models import Prefetch
from .models import Paciente, Exame
from .serializers import PacienteSerializer

def pacientes_view(request):
    """
    View para renderizar a lista de pacientes com seus exames
    """
    pacientes = Paciente.objects.prefetch_related(
        Prefetch('exames', queryset=Exame.objects.order_by('-data'))
    ).order_by('-nivel_gravidade', 'nome')
    
    context = {
        'pacientes': pacientes,
        'total_pacientes': pacientes.count(),
        'pacientes_criticos': pacientes.filter(nivel_gravidade='critico').count()
    }
    return render(request, 'pacientes/lista.html', context)

class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gerenciamento de pacientes
    """
    queryset = Paciente.objects.all().order_by('-nivel_gravidade', 'nome')
    serializer_class = PacienteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'leito', 'nivel_gravidade']
    ordering_fields = ['nome', 'leito', 'nivel_gravidade', 'data_internacao']