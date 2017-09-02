from django.db import models
from django.contrib.auth.models import User


class Cliente(User):
    cpf = models.CharField(unique=True, max_length=11)
    telefone = models.IntegerField()
    nota = models.IntegerField()

    def __str__(self):
        return self.username

