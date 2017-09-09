from django.contrib import admin

# Register your models here.
from models.cliente import Cliente
from models.pizzaria import Pizzaria
from models.pedido import Pedido
from models.pizzas import Pizzas

admin.site.register(Pizzaria)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Pizzas)

