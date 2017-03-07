#coding=utf-8
from estante.models import Pessoa
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.livro import Livro


class DicLivro(View):
    template = 'lista_livros.html'

    def get(self, request):

        livros = Livro.objects.all()

        context_dict = {}
        context_dict['livros'] = livros

        return render(request, self.template, context_dict)

class PerfilLivro(View):
    template = 'perfil_livro.html'

    def get(self, request, id=None):
        print(id)
        livro = Livro.objects.get(pk=id)

        context_dict = {}
        context_dict['livro'] = livro
        context_dict['usuario'] = request.user.id

        return render(request, self.template, context_dict)

class CadastraLivro(View, Pessoa):
    template = 'cad_livro.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
            # MODO CADASTRO
            id = request.POST['id']
            titulo = request.POST['titulo']
            autor = request.POST['autor']
            editora = request.POST['editora']
            ano = request.POST['ano']
            dono = request.user.id

            livro = Livro()

            livro.id_livro = id
            livro.titulo = titulo
            livro.autor = autor
            livro.editora = editora
            livro.ano = ano
            livro.dono = Pessoa.objects.get(pk=dono)

            livro.save()

            return render(request, self.template, {'msg': 'Sucesso no cadastro'})
