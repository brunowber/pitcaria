#coding=utf-8
from estante.models import Pessoa
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.livro import Livro
from estante.models.emprestimo import Emprestimo
from estante.forms.livro import LivroForm, LivroEditaForm

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
        print (id)
        if id:
            livro = Livro.objects.get(id=id)
            form = LivroEditaForm(instance=livro)
        else:
            form = LivroForm()
        return render(request, self.template, {'form': form, 'id': id})

    def post(self, request, id=None):
        print (id)
        if id:
            form = LivroEditaForm(request.POST, instance=Livro.objects.get(id=id))
            if form.is_valid():
                form.save()
                return redirect('/estante/lista_livros')
            else:
                print form.errors
                return render(request, self.template, {'form': form, 'id': id})

        else:
            form = LivroForm(request.POST)
            if form.is_valid():
                livro = form.save(commit=False)
                livro.dono = Pessoa.objects.get(pk=request.user.id)
                livro.status = True
                livro.save()
                return render(request, 'perfil.html', {'msg': "Livro Cadastrado com sucesso!"})
            else:
                print form.errors
        return render(request, 'cad_livro.html', {'form': form})

class Alterar_status_livro(View):
    template = 'perfil_livro.html'

    def post(self, request, id=None):
        user = request.user
        if user.is_authenticated():
            livro = Livro.objects.get(pk=id)
            if livro.status == False:
                livro.status = True
                livro.save()
                return redirect('/estante/livro/' + str(livro.id))
            else:
                livro.status = False
                livro.save()
                return redirect('/estante/livro/' + str(livro.id))
        return render(request, 'index.html')


class Procurar(View):
    template = 'procurar_livro.html'

    def post(self, request):
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        dono = request.POST['dono']
        livros = {}
        pesquisa = []
        livro = Livro.objects
        if dono !='':
            pesquisa = livro.filter(dono__username__icontains=dono)
        if titulo != '':
            pesquisa = livro.filter(titulo__icontains=titulo)
        if autor != '':
            pesquisa = livro.filter(autor__icontains=autor)
        livros['livro'] = pesquisa
        return render(request, self.template, livros)