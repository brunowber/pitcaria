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
        livro = Livro.objects.get(pk=id)

        context_dict = {}
        context_dict['livro'] = livro
        context_dict['usuario'] = request.user.id

        return render(request, self.template, context_dict)

class CadastraLivro(View, Pessoa):
    template = 'cad_livro.html'

    def get(self, request, id=None):
        if id:
            livro = Livro.objects.get(pk=id)
            context_dict = {}
            context_dict['msg'] = 'Atualizar Cadastro'
            context_dict['id'] = id
            context_dict['id_livro'] = livro.id_livro
            context_dict['titulo'] = livro.titulo
            context_dict['autor'] = livro.autor
            context_dict['editora'] = livro.editora
            context_dict['ano'] = livro.ano
            return render(request, 'edita_livro.html', context_dict)
        else:
            return render(request, self.template)

    def post(self, request, id=None):
        print(request.POST['id_livro'])
        id_livro = request.POST['id_livro']
        print('Entrou 2')
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editora = request.POST['editora']
        ano = request.POST['ano']
        if id:
            # MODO EDIÇÃO
            print('entrou')
            livro = Livro.objects.get(pk=id)

            livro.id_livro = id_livro
            livro.titulo = titulo
            livro.autor = autor
            livro.editora = editora
            livro.ano = ano

            livro.save()

            return render(request, 'lista_livros.html')

        else:
            # MODO CADASTRO
            dono = request.user.id

            livro = Livro()

            livro.id_livro = id_livro
            livro.titulo = titulo
            livro.autor = autor
            livro.editora = editora
            livro.ano = ano
            livro.dono = Pessoa.objects.get(pk=dono)

            livro.save()

            return render(request, self.template, {'msg': 'Sucesso no cadastro'})

class Alterar_status_livro(View):
    def get(self, request, id=None):
        user = request.user
        if request.user.is_authenticated():
            livro = Livro.objects.get(pk=id)
            if livro.dono == user.username:
                livro.status = False
                livro.save()
            else:
                return render(request, 'lista_livros.html', {'msg':'Você não é dono deste livro'})
            return render(request, 'index.html')
        return render(request, 'perfil_livro.html')

    def post(self, request, id=None):
        user = request.user
        if request.user.is_authenticated():
            livro = Livro.objects.get(pk=id)
            if livro.dono == user.username:
                livro.status = True
                livro.save()
            else:
                return render(request, 'lista_livros.html', {'msg': 'Você não é dono deste livro'})
            return render(request, 'index.html')