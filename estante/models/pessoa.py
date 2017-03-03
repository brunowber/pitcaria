from django.db import models


class Pessoa(models.Model):
    cpf = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=10)
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    telefone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
