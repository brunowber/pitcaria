# coding=utf-8
from django.views.generic import View
from django.shortcuts import render
from pitcaria.models.pizzaria import *


class ProcurarPizzaria(View):
    template = 'procurar_pizzaria.html'

    def get(self, request):
        pizzaria = Pizzaria.objects.filter()
        return render(request, self.template, {'pizzaria': pizzaria})

    def post(self, request):
        nome = request.POST['procurar']
        pizzaria = Pizzaria.objects.filter(first_name__icontains=nome)
        return render(request, self.template, {'pizzaria': pizzaria})


class Pesquisa(View):
    template = 'pesquisa.html'

    def get(self, request, id=None):

        if id:
            pizzaria = Pizzaria.objects.get(id=id)
            print (pizzaria)
            return render(request, self.template, {'pizzaria': pizzaria})

        return render(request, self.template)
