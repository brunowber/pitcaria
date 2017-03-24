# coding=utf-8
from django import forms
from estante.models import Pessoa
from django.contrib.auth import authenticate


class PessoaForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF')
    endereco = forms.CharField(max_length=30, label='Endereço')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pessoa
        fields = "__all__"
        exclude = ['date_joined']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) != 11:
            raise forms.ValidationError("CPF deve conter 11 dígitos!")
        if cpf.isdigit()== False:
            raise forms.ValidationError('CPF só pode conter números')
        return cpf

    def clean_username(self):
        username = self.cleaned_data['username']
        if Pessoa.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário já existe")
        else:
            return username


class PessoaEditForm(forms.ModelForm):
    cpf = forms.IntegerField(label='CPF')
    endereco = forms.CharField(max_length=30, label='Endereço')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pessoa
        fields = "__all__"
        exclude = ['date_joined', 'username', 'is_active']


    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(str(cpf)) == 11:
            return cpf
        else:
            raise forms.ValidationError("CPF deve conter 11 dígitos!")

    def clean_username(self):
        username = self.cleaned_data['username']
        if Pessoa.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário já existe")
        else:
            return username

class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pessoa
        fields = ('password', 'username',)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if Pessoa.objects.filter(username = username).exists():
            username = Pessoa.objects.get(username=username)
            if authenticate(username=username, password=password) == None:
                raise forms.ValidationError(("Usuario ou senha incorretos"))
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        pessoa = Pessoa.objects.filter(username=username).exists()
        if pessoa:
            return username
        else:
            raise forms.ValidationError('Usuário não existe')