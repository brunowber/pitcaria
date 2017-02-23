from django.contrib import admin

# Register your models here.
from models.pessoa import Pessoa
from models.emprestimo import Emprestimo

admin.site.register(Pessoa)
admin.site.register(Emprestimo)
