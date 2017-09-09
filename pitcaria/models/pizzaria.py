from django.db import models
from django.contrib.auth.models import User


class Pizzaria(User):
    cnpj = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=40)
    complemento = models.CharField(max_length=40)
    telefone = models.IntegerField()
    nota = models.IntegerField()
    User.is_active = models.BooleanField(default=True)
    is_pizzaria = models.BooleanField(default=True)

    def __str__(self):
        return self.username
