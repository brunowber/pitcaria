# -*- coding: utf-8 -*-
from django.db import models
from pitcaria.models.pizzaria import Pizzaria


class Tamanho(models.Model):
    tamanho = models.CharField(max_length=20)
    preco = models.CharField(max_length=20)
    pizzaria = models.ForeignKey(Pizzaria)

    def __str__(self):
        return self.preco

