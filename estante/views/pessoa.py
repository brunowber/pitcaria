# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from estante.models.pessoa import Pessoa
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from estante.forms.pessoa import PessoaForm, PessoaEditForm, SenhaEditForm, LoginForm
from django.core.exceptions import ObjectDoesNotExist

class CadastraPessoa(View):
    template = 'cad_pessoa.html'
    template2 = 'perfil.html'
    template3 = 'index.html'

    def get(self, request):
        id = request.user.id
        if id:
            pessoa = Pessoa.objects.get(pk=id)
            form = PessoaEditForm(instance=pessoa)
        else:
            form = PessoaForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        id = request.user.id
        if id:
            pessoa = Pessoa.objects.get(pk=id)
            form = PessoaEditForm(instance=pessoa, data=request.POST)
            if form.is_valid():
                form.save()
                request.session['first_name'] = pessoa.first_name
                request.session['last_name'] = pessoa.last_name
                request.session['cpf'] = pessoa.cpf
                request.session['endereco'] = pessoa.endereco
                request.session['telefone'] = pessoa.telefone
                request.session['email'] = pessoa.email
                request.session['first_name'] = pessoa.first_name
                return render(request, self.template2, {'msg': 'Informações alteradas com sucesso!'})
            else:
                print(form.errors)
            return render(request, self.template, {'form': form})
        else:
            form = PessoaForm(data=request.POST)
            if form.is_valid():
                form.save()
                pessoa = Pessoa.objects.get(username=request.POST['username'])
                pessoa.set_password(request.POST['password'])
                pessoa.is_active = True
                pessoa.save()
                return render(request, self.template3, {'form': LoginForm})
            else:
                print form.errors
        return render(request, self.template, {'form': form})


class Login(View):
    template = 'index.html'
    template2 = 'perfil.html'
    template3 = 'alterar_status.html'

    def get(self, request):
        form = LoginForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            form = LoginForm(data=request.POST, instance=Pessoa.objects.get(username=username))
        except ObjectDoesNotExist:
            form = LoginForm(data=request.POST)
        print ('cansei')
        if form.is_valid() == False:
            print form.errors
            return render(request, self.template, {'form': form})
        username = form.save(commit = False).username
        password = form.save(commit = False).password

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            pessoa = LoginForm(data=request.POST, instance=Pessoa.objects.get(username=username))
            id = request.user.id
            desativo = Pessoa.objects.get(pk=id)
            if desativo.is_active is False:
                logout(request)
                return render(request, self.template3, {'msg': 'Este usuario está inativo, deseja ativar?', 'form': LoginForm})
            if pessoa.is_valid():
                pessoa = pessoa.save(commit=False)
                request.session['first_name'] = pessoa.first_name
                request.session['last_name'] = pessoa.last_name
                request.session['cpf'] = pessoa.cpf
                request.session['endereco'] = pessoa.endereco
                request.session['telefone'] = pessoa.telefone
                request.session['email'] = pessoa.email
                request.session['first_name'] = pessoa.first_name
                request.session.set_expiry(6000)
                request.session.get_expire_at_browser_close()
                return render(request, self.template2, {'msg': 'Login efetuado com sucesso!'})
            else:
                print pessoa.errors
        else:
            return render(request, self.template, {'form': LoginForm})

class Alterar_status(View):
    template = 'alterar_status.html'
    template2 = 'index.html'

    def get(self, request):
        return render(request, self.template)

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
                    return render(request, self.template2, {'msg': 'usuario ativado com sucesso!'})
                else:
                    return render(request, self.template, {'msg': 'Este usuario já esta ativo'})
            else:
                return render(request, self.template, {'msg': 'Usuario ou senha incorretos'})


class AlterarSenha(View):
    template = 'alterar_senha.html'
    template2 = 'perfil.html'

    def get(self, request):
        form = SenhaEditForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        id = request.user.id
        form = SenhaEditForm(data=request.POST)
        if form.is_valid():
            pessoa = Pessoa.objects.get(pk=id)
            pessoa.set_password(form.password)
            pessoa.save()
            return render(request, self.template2)
        else:
            print form.errors
        return render(request, self.template, {'form': form})