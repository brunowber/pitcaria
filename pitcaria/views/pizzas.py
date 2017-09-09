# coding=utf-8
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from pitcaria.forms.pizzas import *
from pitcaria.models.pizzaria import *
from django.core.exceptions import ObjectDoesNotExist


class CadastraPizzas(View):
    template = 'criar_pizza.html'
    template2 = 'index.html'

    def get(self, request):
        form = PizzasForm()
        print "aqui"
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
    template = 'cardapio.hmtl'

    def get(self, request):
        id = request.user.id
        pizzas = Pizzas.objects.filter(pizzaria=id)
        return render(request, self.template, {'pizzas':pizzas})