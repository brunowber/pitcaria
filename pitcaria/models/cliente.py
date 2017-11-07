# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Cliente(User):
    cpf = models.CharField(unique=True, max_length=11)
    telefone = models.IntegerField()
    data_nascimento= models.DateField()

    def __str__(self):
        return self.username

