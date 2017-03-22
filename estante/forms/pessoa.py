# coding=utf-8
from django import forms
from estante.models import Pessoa


class PessoaForm(forms.ModelForm):
    cpf = forms.IntegerField(label='CPF')
    endereco = forms.CharField(max_length=30, label='Endereço')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pessoa
        fields = "__all__"
        exclude = ['date_joined']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(str(cpf)) == 11:
            return cpf
        else:
            raise forms.ValidationError("CPF deve conter 11 dígitos!")

    def clean_username(self):
        username =  self.cleaned_data['username']
        if Pessoa.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário já existe")
        else:
            return username

class PessoaEditForm(forms.ModelForm):
    cpf = forms.IntegerField(label='CPF')
    endereco = forms.CharField(max_length=30, label='Endereço')
    telefone = forms.IntegerField(label='Telefone')

    class Meta:
        model = Pessoa
        fields = "__all__"
        exclude = ['date_joined', 'password', 'username']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(str(cpf)) == 11:
            return cpf
        else:
            raise forms.ValidationError("CPF deve conter 11 dígitos!")

    def clean_username(self):
        username =  self.cleaned_data['username']
        if Pessoa.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário já existe")
        else:
            return username