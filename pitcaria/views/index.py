# coding=utf-8
from django.views.generic import View
from django.shortcuts import render


class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)
