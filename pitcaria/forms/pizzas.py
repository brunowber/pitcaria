# coding=utf-8

from django import forms
from pitcaria.models.pizzas import Pizzas


class PizzasForm(forms.ModelForm):
    nome = forms.CharField(max_length=40, label='Nome da Pizza')
    sabor = forms.CharField(max_length=40, label='Sabor')
    descricao = forms.CharField(max_length=40, label='Descricao')

    class Meta:

        model = Pizzas
        fields = "__all__"
        exclude = ['pizzaria', ]
