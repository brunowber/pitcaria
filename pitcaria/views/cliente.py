# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from pitcaria.models.cliente import Cliente
from pitcaria.forms.cliente import ClienteForm, ClienteEditForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


class CadastraCliente(View):
    template = 'cad_cliente.html'
    template = 'index.html'

    def get(self, request):
        id = request.user.id
        print (id)
        if id:
            cliente = Cliente.objects.get(pk=id)
            form = ClienteEditForm(instance=cliente)
        else:
            form = ClienteForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        id = request.user.id
        if id:
            cliente = Cliente.objects.get(pk=id)
            form = ClienteEditForm(instance=cliente, data=request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.set_password(request.POST['password'])
                form.is_active = True
                form.save()
                user = authenticate(username=cliente.username, password=request.POST['password'])
                login(request, user)

                request.session['first_name'] = cliente.first_name
                request.session['last_name'] = cliente.last_name
                request.session['cpf'] = cliente.cpf
                request.session['endereco'] = cliente.endereco
                request.session['telefone'] = cliente.telefone
                request.session['email'] = cliente.email
                request.session['first_name'] = cliente.first_name
                request.session['nota'] = cliente.nota

                return render(request, self.template2, {'msg': 'Informações alteradas com sucesso!'})
            else:
                print(form.errors)
            return render(request, self.template, {'form': form})
        else:
            form = ClienteForm(data=request.POST)
            if form.is_valid():
                cliente = form.save(commit=False)
                cliente.set_password(request.POST['password'])
                cliente.is_active = True
                cliente.nota = 0
                cliente.save()

                return render(request, self.template2, {'form': LoginForm})
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
        try:
            form = LoginForm(data=request.POST, instance=Pessoa.objects.get(username=username))
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
            ativo = Cliente.objects.get(username=request.user)
            ativo.is_active = False
            ativo.save()
            logout(request)
            return redirect('/pitcaria/')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                ativo = Cliente.objects.get(username=user)
                if ativo.is_active is False:
                    ativo.is_active = True
                    ativo.save()
                    return render(request, self.template2, {'msg': 'usuario ativado com sucesso!','form':LoginForm})
                else:
                    return render(request, self.template, {'msg': 'Este usuario já esta ativo','form':LoginForm})
            else:
                return render(request, self.template, {'msg': 'Usuario ou senha incorretos','form':LoginForm})