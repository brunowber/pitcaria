#coding=utf-8
from estante.models import Pessoa
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.livro import Livro
from estante.models.emprestimo import Emprestimo


class DicLivro(View):
    template = 'lista_livros.html'

    def get(self, request):
        context_dict = {}
        livros = Livro.objects.all()
        context_dict['livros'] = livros
        emprestimos = []
        for livro in livros:
            emprestimo = Emprestimo.objects.filter(livro_emprestado_id=livro.id).all()
            if emprestimo:
                emprestimos += emprestimo
        context_dict['emprestimos'] = emprestimos
        return render(request, self.template, context_dict)

class PerfilLivro(View):
    template = 'perfil_livro.html'

    def get(self, request, id=None):
        livro = Livro.objects.get(pk=id)
        context_dict = {}
        emprestimo = Emprestimo.objects.filter(livro_emprestado_id=livro.id)
        if emprestimo:
            context_dict['emprestimo'] = emprestimo[0]
        context_dict['livro'] = livro
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

        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editora = request.POST['editora']
        ano = request.POST['ano']
        if id:
            # MODO EDIÇÃO
            livro = Livro.objects.get(pk=id)
            livro.titulo = titulo
            livro.autor = autor
            livro.editora = editora
            livro.ano = ano
            livro.save()
            return redirect('/estante/lista_livros')
        else:
            # MODO CADASTRO
            dono = request.user.id
            id_livro = request.POST['id_livro']
            livro = Livro()

            livro.id_livro = id_livro
            livro.titulo = titulo
            livro.autor = autor
            livro.editora = editora
            livro.ano = ano
            livro.dono = Pessoa.objects.get(pk=dono)

            livro.save()

            return render(request, 'perfil.html', {'msg': 'Livro cadastrado com sucesso!'})

class Alterar_status_livro(View):
    template = 'perfil_livro.html'
    def get(self, request, id=None):
        if id:
            livro = Livro.objects.get(pk=id)
            if livro.status == True:
                livro.status = False
                livro.save()
                return redirect('/estante/livro/'+ str(livro.id))
            else:
                livro.status = True
                livro.save()
                return redirect('/estante/livro/'+ str (livro.id))

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


class Procurar(View):
    template = 'procurar_livro.html'
    def post(self, request):
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        dono = request.POST['dono']
        dono = Pessoa.objects.filter(username = dono)
        livros ={}
        livro = Livro.objects
        if titulo != '':
            livros['livro'] = livro.filter(titulo=titulo)
        if dono:
            livros['livro'] = livro.filter(dono=dono)
        if autor != '':
            livros['livro'] = Livro.objects.filter(autor=autor)

        return render(request, self.template, livros)