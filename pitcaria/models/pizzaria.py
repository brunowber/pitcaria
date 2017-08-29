from django.db import models
from django.contrib.auth.models import User


class Pizzaria(User):
    cnpj = models.IntegerField(max_length=14, primary_key=True)
    estado = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=40)
    complemento = models.CharField(max_length=40)
    telefone = models.IntegerField(max_length=10)
    nota = models.IntegerField(max_length=2)
    User.is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
