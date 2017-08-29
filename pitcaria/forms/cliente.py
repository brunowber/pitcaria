# coding=utf-8

from pitcaria.forms.validators.pessoa_validator import *
from django import forms
from django.contrib.auth import authenticate
from pitcaria.models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=254, label='Nome de Usuário')
    first_name = forms.CharField(max_length=40, label='Nome')
    last_name = forms.CharField(max_length=40, label='Sobrenome')
    cpf = forms.CharField(label='CPF')
    data_nascimento = forms.CharField(max_length=10, label='Data de Nascimento')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['date_joined', 'nota', 'is_active']

    def clean_cpf(self):
        return CpfValidator(self.cleaned_data[str('cpf')])

    def clean_username(self):
        username=self.cleaned_data['username']
        if Cliente.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuário já existe')
        return username

    def clean_first_name(self):
        return NameValidator(self.cleaned_data['first_name'])

    def clean_last_name(self):
        return NameValidator(self.cleaned_data['last_name'])

class ClienteEditForm(forms.ModelForm):
    first_name=forms.CharField(max_length=40, label='Nome')
    last_name=forms.CharField(max_length=40, label='Sobrenome')
    data_nascimento=forms.CharField(max_length=10, label='Data de Nascimento')
    cpf = forms.IntegerField(label='CPF')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['date_joined', 'username', 'is_active', 'nota']

    def clean_cpf(self):
        return CpfValidator(self.cleaned_data[str('cpf')])

    def clean_first_name(self):
        return NameValidator(self.cleaned_data['first_name'])

    def clean_last_name(self):
        return NameValidator(self.cleaned_data['last_name'])

class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = ('password', 'username',)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if Cliente.objects.filter(username = username).exists():
            username = Cliente.objects.get(username=username)
            if authenticate(username=username, password=password) == None:
                raise forms.ValidationError(("Usuario ou senha incorretos"))
        return self.cleaned_data

    def clean_username(self):
        return UsernameValidator(self.cleaned_data['username'])
