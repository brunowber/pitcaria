from django.db import models
from django.contrib.auth.models import User


class Pessoa(User):
    cpf = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=30)
    telefone = models.IntegerField()
    User.is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
