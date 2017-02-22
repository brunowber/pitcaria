from django.db import models

class Pessoa(models.Model):
    cpf = models.IntegerField(max_length=11)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    telefone = models.IntegerField(max_length=11)
    email = models.EmailField()