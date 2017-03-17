from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.emprestimo import Emprestimo
from estante.models.livro import Livro
from estante.models.pessoa import Pessoa
from django.shortcuts import render
from datetime import date


class Cad_emprestimo(View):
    def get(self, request, id=None):
        livro = Livro.objects.get(pk=id)
        pessoa = Pessoa.objects.get(pk=request.user.id)
        emprestimo = Emprestimo()
        emprestimo.dt_emprest = date.today()
        emprestimo.dt_devol = date.fromordinal(date.today().toordinal() + 15)
        emprestimo.livro_emprestado = livro
        emprestimo.pegou_emprestado = pessoa

        emprestimo.save()

        livro.status = False
        livro.save()

        return render(request, 'perfil.html')

class Devolver(View):
    def get(self, request, id=None):
        emprestimo = Emprestimo.objects.get(pk=id)
        livro = Livro.objects.get(pk=emprestimo.livro_emprestado_id)

        livro.status = True
        livro.save()

        emprestimo.delete()

        return render(request, 'perfil.html')