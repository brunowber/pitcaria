# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from pitcaria.models.cliente import Cliente
from pitcaria.models.pedido import Pedido
from pitcaria.models.pizzaria import Pizzaria
from pitcaria.forms.cliente import ClienteForm
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
                # request.session['endereco'] = cliente.endereco
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

                return render(request, self.template2, {'msg': 'Conta criada com sucesso!'})
            else:
                print form.errors
        return render(request, self.template, {'form': form})


class Historico(View):
    template = 'historico_cliente.html'

    def get(self, request):
        pedidos = Pedido.objects.filter(cliente_id=request.user.id)
        return render(request, self.template, {'pedidos': pedidos})


class Nota(View):
    template = 'historico_cliente.html'

    def post(self, request, id=None):
        print request.POST['estrela']
        estrela = request.POST['estrela']
        pedido = Pedido.objects.get(id=id)
        pedido.is_votado = True
        pizzaria = Pizzaria.objects.get(id=pedido.pizzaria.id)
        pizzaria.nota = pizzaria.nota+ int(estrela)
        pizzaria.quant_nota += 1
        pizzaria.nota_real = pizzaria.nota / pizzaria.quant_nota
        pizzaria.save()
        pedido.save()
        pedidos = Pedido.objects.filter(cliente_id=request.user.id)
        return render(request, self.template, {'pedidos': pedidos})
