from estante.models import Pessoa
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.pessoa import Pessoa

class CadastraPessoa(View):

    template='cad_pessoa.html'

    def get(self, request):
        return render(request, self.template, {'willian_bobao':'oi, Bruna, voce esta entendendo alguma coisa?'})


    def post(self,request):
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        telefone = request.POST['telefone']
        email = request.POST['email']

        pessoa = Pessoa()

        pessoa.nome = nome
        pessoa.cpf = cpf
        pessoa.endereco = endereco
        pessoa.telefone = telefone
        pessoa.email = email

        pessoa.save()

        return redirect('/cad_pessoa/')
