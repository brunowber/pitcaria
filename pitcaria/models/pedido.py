from django.db import models
from pitcaria.models.pizzaria import Pizzaria
from pitcaria.models.cliente import Cliente
from pitcaria.models.tamanho import Tamanho
from pitcaria.models.pizzas import Pizzas


class Pedido(models.Model):
    entrega = models.CharField(max_length=100)
    horario = models.DateField()
    pizzaria = models.ForeignKey(Pizzaria)
    cliente = models.ForeignKey(Cliente)
    primeiro = models.ForeignKey(Pizzas, related_name='primeiro')
    segundo = models.ForeignKey(Pizzas, related_name='segundo')
    terceiro = models.ForeignKey(Pizzas, related_name='terceiro')
    tamanho = models.ForeignKey(Tamanho)
    is_votado = models.BooleanField()

    def __str__(self):
        return self.entrega
