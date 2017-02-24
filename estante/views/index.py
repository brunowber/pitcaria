from estante.models import Pessoa
from django.views.generic import View
from django.shortcuts import render, redirect
from estante.models.pessoa import Pessoa


class Logar(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        return redirect('/estante/cad_livro/')


