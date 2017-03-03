#coding=utf-8
from django.views.generic import View
from django.shortcuts import render
from estante.models.pessoa import Pessoa


class CadastraPessoa(View):

    template='cad_pessoa.html'

    def get(self, request):
        # if request.POST['id']:
            # MODO EDIÇÃO (JÁ EXISTE OBJETO NO BD)
        return render(request, self.template, {'msg': 'Novo cadastro'})


    def post(self, request):

        if request.POST['id']:
            # MODO EDIÇÃO
            return render(request, self.template, {'msg': 'Modo edição'})
        else:
            # MODO CADASTRO
            usuario = request.POST['login']
            if Pessoa.objects.filter(login=usuario).exists():
                return render(request, self.template, {'msg': 'Erro login ja existente'})

            nome = request.POST['nome']
            senha = request.POST['senha']
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
            pessoa.login = usuario
            pessoa.senha = senha

            pessoa.save()

            return render(request, self.template, {'msg': 'Sucesso no cadastro'})