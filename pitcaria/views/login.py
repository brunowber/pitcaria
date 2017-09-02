# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from pitcaria.models.pizzaria import *
from pitcaria.models.cliente import *
from pitcaria.forms.login import *
from django.core.exceptions import ObjectDoesNotExist


class Login(View):
    template = 'index.html'
    template2 = 'index.html'

    def get(self, request):
        form = LoginForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        username = request.POST['username']
        if request.POST['checkbox'] == "cliente":
            try:
                form = LoginForm(data=request.POST, instance=Cliente.objects.get(username=username))
            except ObjectDoesNotExist:
                form = LoginForm(data=request.POST)
            if not form.is_valid():
                print form.errors
                return render(request, self.template, {'form': form})
            username = form.save(commit=False).username
            password = form.save(commit=False).password
            print (username, password)
            user = authenticate(username=username, password=password)
            print user
            if user:
                login(request, user)
                cliente = LoginForm(data=request.POST, instance=Cliente.objects.get(username=username))
                id = request.user.id
                if cliente.is_valid():
                    cliente = cliente.save(commit=False)
                    request.session['first_name'] = cliente.first_name
                    request.session['last_name'] = cliente.last_name
                    request.session['cpf'] = cliente.cpf
                    request.session['telefone'] = cliente.telefone
                    request.session['nota'] = cliente.nota
                    return render(request, self.template2, {'msg': 'Login efetuado com sucesso!'})
                else:
                    print cliente.errors
        else:
            return render(request, self.template, {'form': LoginForm})
