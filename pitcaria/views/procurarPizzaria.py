# coding=utf-8
from django.views.generic import View
from django.shortcuts import render
from pitcaria.models.pizzaria import *


class ProcurarPizzaria(View):
    template = 'procurar_pizzaria.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        nome = request.POST['procurar']
        pizzaria = Pizzaria.objects.filter(first_name__icontains=nome)
        print "pesquisa:", pizzaria
        return render(request, self.template, {'pizzaria': pizzaria})
