# coding=utf-8
from time import timezone

import datetime
from django.views.generic import View
from django.shortcuts import render
from pitcaria.forms.pizzas import *
from pitcaria.forms.pedido import *
from pitcaria.models.tamanho import *
from pitcaria.models.cliente import *
from pitcaria.models.pedido import *


class FazerPedido(View):
    template = 'fazer_pedido.html'
    template2 = 'index.html'

    def get(self, request, id=None):
        form = PedidoForm()
        return render(request, self.template, {'form': form, 'id': id})

    def post(self, request, id=None):
        form = PedidoForm(data=request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            print (id)
            pedido.pizzaria=Pizzaria.objects.get(id=id)
            pedido.horario=datetime.datetime.now()
            pedido.cliente=Cliente.objects.get(id=request.user.id)
            pedido.is_votado= False
            pedido.save()
            return render(request, self.template2, {'msg': "Pedido realizado com sucesso"})
        else:
            print form.errors
            return form.errors
