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
    template2 = 'index.html'

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
