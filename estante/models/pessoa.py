from django.db import models
from django.contrib.auth.models import User


class Pessoa(User):
    cpf = models.CharField(unique=True, max_length=11)
    endereco = models.CharField(max_length=30)
    telefone = models.IntegerField()
    User.is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
