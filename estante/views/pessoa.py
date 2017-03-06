#coding=utf-8
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.pessoa import Pessoa
from django.contrib.auth import authenticate, login, logout

def logout_view(request):
    logout(request)
    return render(request, 'index.html')


class Perfil(View):
    template = 'perfil.html'

    def get(self, request):
        return render(request, self.template, {})


class CadastraPessoa(View):

    template = 'cad_pessoa.html'

    def get(self, request):
        id = request.user.id
        if id:
            # MODO EDIÇÃO (JÁ EXISTE OBJETO NO BD)
            pessoa = Pessoa.objects.get(pk=id)
            context_dict = {}
            context_dict['msg'] = 'Atualizar Cadastro'
            context_dict['username'] = pessoa.username
            context_dict['first_name'] = pessoa.first_name
            context_dict['last_name'] = pessoa.last_name
            context_dict['cpf'] = pessoa.cpf
            context_dict['endereco'] = pessoa.endereco
            context_dict['telefone'] = pessoa.telefone
            context_dict['email'] = pessoa.email
            return render(request, 'edita_pessoa.html', context_dict)
        else:
            return render(request, self.template, {'msg': 'Novo Cadastro'})


    def post(self, request):

        id = request.user.id
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        telefone = request.POST['telefone']
        email = request.POST['email']
        if id:
            #MODO EDIÇÃO
            pessoa = Pessoa.objects.get(pk=id)

            pessoa.first_name = first_name
            pessoa.last_name = last_name
            pessoa.cpf = cpf
            pessoa.endereco = endereco
            pessoa.telefone = telefone
            pessoa.email = email

            pessoa.save()

            return render(request, 'perfil.html', {'msg': 'Informações alteradas com sucesso!'})
        else:
            #MODO CADASTRO
            usuario = request.POST['username']
            if Pessoa.objects.filter(username=usuario).exists():
                return render(request, self.template, {'msg': 'Erro, login ja existe'})

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

            return redirect('perfil/')


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
            return redirect('perfil/')
        else:
            return render(request, self.template, {'msg': 'Erro'})


class Alterar_status(View):
# não esta funcionando a parte de reativar o usuario
    def get(self, request):
        id = request.user.id
        if id:
            desativo = Pessoa.objects.get(pk=id)
            desativo.is_active = False
            desativo.save()
            return redirect('/')
        else:
            return render (request, 'alterar_status.html')

    def post(self, request):
        id = request.user.id
        if id is None:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                ativo = Pessoa.objects.get(username=username)
                ativo.is_active = True
                ativo.save()
                return redirect('/')
        else:
            return redirect('/')
