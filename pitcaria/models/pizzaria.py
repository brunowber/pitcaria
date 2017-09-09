from django.db import models
from django.contrib.auth.models import User


class Pizzaria(User):
    cnpj = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=40)
    complemento = models.CharField(max_length=40)
    obs = models.CharField(max_length=100)
    telefone = models.IntegerField()
    nota = models.IntegerField()
    quant_nota = models.IntegerField()
    nota_real = models.IntegerField()
    User.is_active = models.BooleanField(default=True)
    is_pizzaria = models.BooleanField(default=True)

    def __str__(self):
        return self.username
