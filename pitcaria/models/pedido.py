from django.db import models
from pitcaria.models.pizzaria import Pizzaria
from pitcaria.models.cliente import Cliente


class Pedido(models.Model):
    tamanho = models.CharField(max_length=20)
    preco = models.CharField(max_length=30)
    entrega = models.CharField(max_length=30)
    pizzaria = models.ForeignKey(Pizzaria)
    cliente = models.ForeignKey(Cliente)

    def __str__(self):
        return self.entrega
