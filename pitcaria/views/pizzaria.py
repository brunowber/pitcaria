# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from pitcaria.models.pizzaria import *
from pitcaria.forms.pizzaria import *
from django.core.exceptions import ObjectDoesNotExist


class CadastraPizzaria(View):
    template = 'cad_pizzaria.html'
    template2 = 'cad_pizzaria.html'

    def get(self, request):
        id = request.user.id
        if id:
            pizzaria = Pizzaria.objects.get(pk=id)
            form = PessoaEditForm(instance=pizzaria)
        else:
            form = PizzariaForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        id = request.user.id
        if id:
            pizzaria = Pizzaria.objects.get(pk=id)
            form = PessoaEditForm(instance=pizzaria, data=request.POST)
            print (form)
            if form.is_valid():
                form = form.save(commit=False)
                form.set_password(request.POST['password'])
                form.is_active = True
                form.save()
                user = authenticate(username=pizzaria.username, password=request.POST['password'])
                login(request, user)

                request.session['first_name'] = pizzaria.first_name
                #request.session['last_name'] = pizzaria.last_name
                request.session['cnpj'] = pizzaria.cnpj
                request.session['cidade'] = pizzaria.cidade
                request.session['bairro'] = pizzaria.bairro
                request.session['rua'] = pizzaria.rua
                request.session['complemento'] = pizzaria.complemento
                request.session['telefone'] = pizzaria.telefone
                request.session['email'] = pizzaria.email
                return render(request, self.template2, {'msg': 'Informações alteradas com sucesso!'})
            else:
                print(form.errors)
            return render(request, self.template, {'form': form})
        else:
            form = PizzariaForm(data=request.POST)
            if form.is_valid():
                pessoa = form.save(commit=False)
                pessoa.set_password(request.POST['password'])
                pessoa.is_active = True
                pessoa.save()

                return render(request, self.template3, {'form': LoginForm})
            else:
                print form.errors
        return render(request, self.template, {'form': form})


class Login(View):
    template = 'index.html'

    def get(self, request):
        form = LoginForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        username = request.POST['username']
        try:
            form = LoginForm(data=request.POST, instance=Cliente.objects.get(username=username))
        except ObjectDoesNotExist:
            form = LoginForm(data=request.POST)
        if not form.is_valid():
            print form.errors
            return render(request, self.template, {'form': form})
        username = form.save(commit=False).username
        password = form.save(commit=False).password

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
        return render(request, self.template, {'form':LoginForm})

    def post(self, request):
        if request.user.id:
            ativo = Pessoa.objects.get(username=request.user)
            ativo.is_active = False
            ativo.save()
            logout(request)
            return redirect('/pitcaria/')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                ativo = Pessoa.objects.get(username=user)
                if ativo.is_active is False:
                    ativo.is_active = True
                    ativo.save()
                    return render(request, self.template2, {'msg': 'usuario ativado com sucesso!','form':LoginForm})
                else:
                    return render(request, self.template, {'msg': 'Este usuario já esta ativo','form':LoginForm})
            else:
                return render(request, self.template, {'msg': 'Usuario ou senha incorretos','form':LoginForm})