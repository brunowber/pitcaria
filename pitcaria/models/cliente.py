from django.db import models
from django.contrib.auth.models import User


class Cliente(User):
    cpf = models.CharField(unique=True, max_length=11)
    telefone = models.IntegerField()
    data_nascimento = models.DateField()
    nota = models.IntegerField()
    User.is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
