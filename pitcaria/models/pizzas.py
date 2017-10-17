from django.db import models
from pitcaria.models.pizzaria import Pizzaria


class Pizzas(models.Model):
    nome = models.CharField(max_length=255)
    sabor = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1000)
    pizzaria = models.ForeignKey(Pizzaria)

    def __str__(self):
        return self.nome
