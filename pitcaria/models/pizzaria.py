from django.db import models
from django.contrib.auth.models import User


class Pizzaria(User):
    cnpj = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    complemento = models.CharField(blank=True, max_length=100)
    obs = models.CharField(blank=True, max_length=100)
    telefone = models.IntegerField()
    nota = models.IntegerField()
    quant_nota = models.IntegerField()
    nota_real = models.IntegerField()
    User.is_active = models.BooleanField(default=True)
    is_pizzaria = models.BooleanField(default=True)

    def __str__(self):
        return self.username
