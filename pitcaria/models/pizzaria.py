from django.db import models
from django.contrib.auth.models import User


class Pizzaria(User):
    cidade = models.CharField(max_length=40)
    bairro = models.CharField(max_length=40)
    rua = models.CharField(max_length=40)
    complemento = models.CharField(max_length=40)
    cnpj = models.IntegerField(max_length=10)
    telefone = models.IntegerField()
    User.is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
