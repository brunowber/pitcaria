# coding=utf-8

from django import forms
from pitcaria.models.tamanho import Tamanho
from pitcaria.models.pizzas import Pizzas
from pitcaria.models.pedido import Pedido


class PedidoForm(forms.ModelForm):
    entrega = forms.CharField(max_length=40, label='Endereco')
    tamanho = forms.ModelChoiceField(queryset=Tamanho.objects.all(), label='Tamanho')
    primeiro = forms.ModelChoiceField(queryset=Pizzas.objects.all(), label='Sabor 1')
    segundo = forms.ModelChoiceField(queryset=Pizzas.objects.all(), label='Sabor 2')
    terceiro = forms.ModelChoiceField(queryset=Pizzas.objects.all(), label='Sabor 3')

    class Meta:

        model = Pedido
        fields = "__all__"
        exclude = ['pizzaria', 'cliente', 'horario', ]
