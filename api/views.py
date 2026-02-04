from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework.decorators import api_view
from .serializers import ( UsuarioSerializer, 
                          ImovelSerializer, 
                          ContratoSerializer, 
                          PagamentoSerializer
)
# class UsuarioListCreateView(ListCreateAPIView):
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)

######### GET E POST USUARIOS #########
class UsuarioListCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
######### GET  E POST ###########
@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
        queryset = Usuario.objects.all()
        serializers = UsuarioSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = UsuarioSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
####### GET E POST IMOVEL ###########
class ImovelListCreateView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

######### GET E POST CONTRATO #########
class ContratoListCreateView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

######## GET E POST PAGAMENTO #########
class PagamentoListCreateView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

######### UPDATE E DELETE USUARIOS #########
class UsuarioUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'

class ImovelUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    lookup_field = 'id'

class ContratoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    lookup_field = 'id' 

class PagamentoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    lookup_field = 'id'