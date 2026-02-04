from django.urls import path
from .views import ImovelUpdateDestroyView, UsuarioListCreateView, UsuarioUpdateDestroyView, ImovelListCreateView, ContratoListCreateView, ContratoUpdateDestroyView, PagamentoListCreateView, PagamentoUpdateDestroyView, listar_usuarios

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view()),
    path('usuarios/<int:pk>/', UsuarioUpdateDestroyView.as_view()),
    path('users', listar_usuarios),

    path('imoveis/', ImovelListCreateView.as_view()),
    path('imoveis/<int:pk>/', ImovelListCreateView.as_view()),
    path('imoveis/<int:pk>/', ImovelUpdateDestroyView.as_view()),

    path('contratos/', ContratoListCreateView.as_view()),
    path('contratos/<int:pk>/', ContratoUpdateDestroyView.as_view()),

    path('pagamentos/', PagamentoListCreateView.as_view()),
    path('pagamentos/<int:pk>/', PagamentoUpdateDestroyView.as_view()),

    
     

]