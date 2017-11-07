# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from models.cliente import Cliente
from models.pizzaria import Pizzaria
from models.pedido import Pedido
from models.pizzas import Pizzas
from models.tamanho import Tamanho

admin.site.register(Pizzaria)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Pizzas)
admin.site.register(Tamanho)

