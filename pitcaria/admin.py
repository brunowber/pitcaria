from django.contrib import admin

# Register your models here.
from models.cliente import Cliente
from models.pizzaria import Pizzaria

admin.site.register(Pizzaria)
admin.site.register(Cliente)

