from django.db import models
from estante.models.pessoa import Pessoa

class Emprestimo(models.Model):
    dt_emprest = models.DateField()
    dt_devol = models.DateField()
    #livro_emprestado = models.ForeignKey()
    pegou_emprestado = models.ForeignKey(Pessoa)