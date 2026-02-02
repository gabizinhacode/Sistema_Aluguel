from django.db import models


class Usuario(models.Model):
    TIPO_CHOICES = [
        ('locador', 'Locador'),
        ('locatorio', 'Locatorio'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)  #locador ou locatorio

    def __str__(self):
        return self.nome
    
class Imovel(models.Model):

    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alugado', 'Alugado'),
    ]
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    #chave estrangeira 
    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='imoveis')

    def __str__(self):
        return self.titulo
    
class Contrato(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contratos')
    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_locador')
    locatorio = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_locatorio')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return f"Contrato {self.id} - {self.imovel.titulo}"
        
class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)  #pago ou pendente

    def __str__(self):
        return f"Pagamento {self.id} - Contrato {self.contrato.id}"