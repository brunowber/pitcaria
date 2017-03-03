#coding=utf-8
from django.views.generic import View
from django.shortcuts import render
from estante.models.pessoa import Pessoa
from django.contrib.auth import authenticate, login


class CadastraPessoa(View):

    template='cad_pessoa.html'

    def get(self, request):
        # if request.POST['id']:
            # MODO EDIÇÃO (JÁ EXISTE OBJETO NO BD)
        return render(request, self.template, {'msg': 'Novo cadastro'})


    def post(self, request):

        #if request.POST['id']:
            # MODO EDIÇÃO
            #return render(request, self.template, {'msg': 'Modo edição'})
        #else:
            # MODO CADASTRO
        usuario = request.POST['username']
        if Pessoa.objects.filter(username=usuario).exists():
            return render(request, self.template, {'msg': 'Erro login ja existente'})

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        telefone = request.POST['telefone']
        email = request.POST['email']

        pessoa = Pessoa()

        pessoa.first_name = first_name
        pessoa.last_name = last_name
        pessoa.cpf = cpf
        pessoa.endereco = endereco
        pessoa.telefone = telefone
        pessoa.email = email
        pessoa.username = usuario
        pessoa.set_password(password)

        pessoa.save()

        return render(request, self.template, {'msg': 'Sucesso no cadastro'})


class Login(View):

    template = 'index.html'

    def get(self, request):
        return render(request, self.template )

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, self.template, {'msg': 'Sucesso'})
        else:
            return render(request, self.template, {'msg': 'Erro'})


class Desativar(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        id = request.POST['id']
        inativo = Pessoa.objects.get(id=id)
        inativo.is_active = False
        inativo.save()
        return render(request, self.template)