# coding=utf-8

from django import forms
from django.contrib.auth import authenticate
from pitcaria.models.pizzaria import Pizzaria


class PizzariaForm(forms.ModelForm):
    first_name = forms.CharField(max_length=40, label='Nome da Pizzaria')
    cidade = forms.CharField(max_length=40, label='Cidade')
    bairro = forms.CharField(max_length=40, label='Bairro')
    rua = forms.CharField(max_length=40, label='Rua')
    complemento = forms.CharField(max_length=40, label='Complemento')
    obs = forms.CharField(max_length=40, label='Observacao')
    cnpj = forms.IntegerField(label='CNPJ')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        #def clean_cpf(self):
         #   return CpfValidator(self.cleaned_data[str('cpf')])

       # def clean_username(self):
        #    username = self.cleaned_data['username']
         #   if Pizzaria.objects.filter(username=username).exists():
          #      raise forms.ValidationError('Usuário já existe')
           # return username

        model = Pizzaria
        fields = "__all__"
        exclude = ['date_joined', 'nota', 'last_name', 'nota_real', 'quant_nota', ]



    #def clean_first_name(self):
     #   return NameValidator(self.cleaned_data['first_name'])


class PessoaEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=40, label='Nome da Pizzaria')
    cidade = forms.CharField(max_length=40, label='Cidade')
    bairro = forms.CharField(max_length=40, label='Bairro')
    rua = forms.CharField(max_length=40, label='Rua')
    complemento = forms.CharField(max_length=40, label='Complemento')
    cnpj = forms.IntegerField(label='CNPJ')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pizzaria
        fields = "__all__"
        exclude = ['date_joined', 'username', 'is_active', 'nota']

   # def clean_cpf(self):
    #    return CpfValidator(self.cleaned_data[str('cpf')])

    #def clean_first_name(self):
     #   return NameValidator(self.cleaned_data['first_name'])


class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pizzaria
        fields = ('password', 'username',)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if Pizzaria.objects.filter(username=username).exists():
            username = Pizzaria.objects.get(username=username)
            if authenticate(username=username, password=password) is None:
                raise forms.ValidationError(("Usuario ou senha incorretos"))
        return self.cleaned_data

    #def clean_username(self):
        #return UsernameValidator(self.cleaned_data['username'])
