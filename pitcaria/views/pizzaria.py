# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from pitcaria.models.pedido import *
from pitcaria.forms.pizzaria import *
from django.core.exceptions import ObjectDoesNotExist


class CadastraPizzaria(View):
    template = 'cad_pizzarias.html'
    template2 = 'cad_pizzaria.html'
    template3 = 'index.html'

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

                request.session['id'] = pizzaria.id
                request.session['first_name'] = pizzaria.first_name
                #request.session['last_name'] = pizzaria.last_name
                request.session['cnpj'] = pizzaria.cnpj
                request.session['cidade'] = pizzaria.cidade
                request.session['estado'] = pizzaria.cidade
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
                pizzaria = form.save(commit=False)
                pizzaria.set_password(request.POST['password'])
                pizzaria.set_password(request.POST['password'])
                pizzaria.is_active = True
                pizzaria.nota = 0
                pizzaria.nota_real = 0
                pizzaria.quant_nota = 0
                pizzaria.is_pizzaria = True
                pizzaria.save()

                return render(request, self.template3, {'form': LoginForm})
            else:
                print form.errors
        return render(request, self.template, {'form': form})


class HistoricoPizzaria(View):
    template = 'historico_pizzaria.html'

    def get(self, request):
        id= Pizzaria.objects.get(id=request.user.id)
        pedidos = Pedido.objects.filter(pizzaria_id=id).order_by("-id")
        return render(request, self.template, {'pedidos': pedidos})
