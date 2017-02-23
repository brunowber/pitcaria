from estante.models import Pessoa
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.livro import Livro


class CadastraLivro(View,Pessoa):

    template='cad_livro.html'

    def get(self, request):
        return render(request, self.template, {'willian_bobao':'oi, Bruna, voce esta entendendo alguma coisa?'})


    def post(self,request):
        id = request.POST['id']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editora = request.POST['editora']
        ano = request.POST['ano']
        dono = request.POST['dono']

        livro = Livro()

        livro.id_livro = id
        livro.titulo = titulo
        livro.autor = autor
        livro.editora = editora
        livro.ano = ano
        livro.dono = Pessoa.objects.get(cpf=dono)

        livro.save()

        return redirect('/cad_livro/')
