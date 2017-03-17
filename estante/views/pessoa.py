# coding=utf-8
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.pessoa import Pessoa
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

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
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        telefone = request.POST['telefone']
        email = request.POST['email']
        if id:
            # MODO EDIÇÃO
            pessoa = Pessoa.objects.get(pk=id)

            pessoa.first_name = first_name
            pessoa.last_name = last_name
            pessoa.cpf = cpf
            pessoa.endereco = endereco
            pessoa.telefone = telefone
            pessoa.email = email
            pessoa.save()

            request.session['first_name'] = pessoa.first_name
            request.session['last_name'] = pessoa.last_name
            request.session['cpf'] = pessoa.cpf
            request.session['endereco'] = pessoa.endereco
            request.session['telefone'] = pessoa.telefone
            request.session['email'] = pessoa.email
            request.session['first_name'] = pessoa.first_name
            return render(request, 'perfil.html', {'msg': 'Informações alteradas com sucesso!'})
        else:
            # MODO CADASTRO
            usuario = request.POST['username']
            if Pessoa.objects.filter(username=usuario).exists() or Pessoa.objects.filter(cpf=cpf).exists():
                return render(request, self.template, {'msg': 'Erro, Usuario ou cpf ja existente'})
            password = request.POST['password']
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

            return render(request, 'index.html')


class Login(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            pessoa = Pessoa.objects.get(username=username)
            id = request.user.id
            desativo = Pessoa.objects.get(pk=id)
            if desativo.is_active is False:
                logout(request)
                return render(request, 'alterar_status.html', {'msg': 'Este usuario está inativo, deseja ativar?'})
            request.session['first_name'] = pessoa.first_name
            request.session['last_name'] = pessoa.last_name
            request.session['cpf'] = pessoa.cpf
            request.session['endereco'] = pessoa.endereco
            request.session['telefone'] = pessoa.telefone
            request.session['email'] = pessoa.email
            request.session['first_name'] = pessoa.first_name
            request.session.set_expiry(600)
            request.session.get_expire_at_browser_close()

            return render(request, 'perfil.html', {'msg':'Login efetuado com sucesso!'})
        else:
            return render(request, self.template, {'msg': 'Erro usuario ou senha incorretos'})


class Alterar_status(View):
    def get(self, request):
        return render(request, 'alterar_status.html')

    def post(self, request):
        if request.user.id:
            ativo = Pessoa.objects.get(username=request.user)
            ativo.is_active = False
            ativo.save()
            logout(request)
            return redirect('/estante/')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                ativo = Pessoa.objects.get(username=user)
                if ativo.is_active is False:
                    ativo.is_active = True
                    ativo.save()
                    return render(request, 'index.html', {'msg': 'usuario ativado com sucesso!'})
                else:
                    return render(request, 'alterar_status.html', {'msg': 'Este usuario já esta ativo'})
            else:
                return render(request, 'alterar_status.html', {'msg': 'Usuario ou senha incorretos'})