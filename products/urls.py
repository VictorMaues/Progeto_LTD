from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, pacientes_view  # Adicione todas as views necessárias

# Configuração do Router para API
router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='paciente')  # Adicionei basename

urlpatterns = [
    # Rotas da API
    path('api/', include(router.urls)),  # Agrupa todas as rotas da API sob /api/
    
    # Rota para a view tradicional (se necessário)
    path('pacientes/', pacientes_view, name='pacientes-html'),  # Nome único para evitar conflitos
]