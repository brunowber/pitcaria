# coding=utf-8
from django import forms
from estante.models import Pessoa

class PessoaForm(forms.Form):
    cpf = forms.IntegerField(label='CPF')
    endereco = forms.CharField(max_length=30, label='Endereço')
    telefone = forms.IntegerField(label='Telefone')
    username = forms.CharField(max_length=12, label='Login')
    first_name = forms.CharField(max_length=50, label='Nome')
    last_name = forms.CharField(max_length=50, label='Sobrenome')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = Pessoa
        fields = "__all__"

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(str(cpf)) == 11:
            return cpf
        else:
            raise forms.ValidationError("CPF deve conter 11 dígitos!")