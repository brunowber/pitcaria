# coding=utf-8
from django import forms

class PessoaForm(forms.Form):
    cpf = forms.IntegerField(max_length=11, label='CPF')
    endereco = forms.CharField(max_length=30, label='Endereço')
    telefone = forms.IntegerField(max_length=11, label='Telefone')
    username = forms.CharField(max_length=12, label='Login')
    first_name = forms.CharField(max_length=50, label='Nome')
    last_name = forms.CharField(max_length=50, label='Sobrenome')
    email = forms.EmailField(label='E-mail')
