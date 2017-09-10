# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from pitcaria.forms.pizzas import *
from pitcaria.forms.tamanho import *
from pitcaria.models.tamanho import *
from django.core.exceptions import ObjectDoesNotExist


class CadastraPizzas(View):
    template = 'criar_pizza.html'
    template2 = 'index.html'

    def get(self, request):
        form = PizzasForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = PizzasForm(data=request.POST)
        if form.is_valid():
            pizzas = form.save(commit=False)
            pizzas.pizzaria=Pizzaria.objects.get(id=request.user.id)
            pizzas.save()
            return render(request, self.template2)
        else:
            print form.errors
            return form.errors


class Cardapio(View):
    template = 'cardapio.html'

    def get(self, request, id=None):
        if not id:
            id = request.user.id
        pizzas = Pizzas.objects.filter(pizzaria=Pizzaria.objects.get(id=id))
        return render(request, self.template, {'pizzas': pizzas, 'id': id})


class DefPedido(View):
    template = 'def_pedido.html'
    template2 = 'index.html'

    def get(self, request):

        form = TamanhoForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = TamanhoForm(data=request.POST)
        print TamanhoForm
        print (request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.pizzaria=Pizzaria.objects.get(id=request.user.id)
            print Pizzaria.objects.get(id=request.user.id)
            pedido.save()
            return render(request, self.template2)
        else:
            print form.errors
            return form.errors
