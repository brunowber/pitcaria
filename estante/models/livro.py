from django.db import models
from estante.models.pessoa import Pessoa

class Livro(models.Model):
    id_livro = models.IntegerField()
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    editora = models.CharField(max_length=30)
    ano = models.IntegerField()
    dono = models.ForeignKey(Pessoa)
