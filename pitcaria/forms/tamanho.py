# coding=utf-8

from django import forms
from pitcaria.models.tamanho import Tamanho


class TamanhoForm(forms.ModelForm):
    tamanho = forms.CharField(max_length=40, label='Tamanho da Pizza')
    preco = forms.IntegerField(label='Preco')

    class Meta:

        model = Tamanho
        fields = "__all__"
        exclude = ['pizzaria', ]
