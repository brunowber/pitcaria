# coding=utf-8

from django import forms
from django.contrib.auth import authenticate
from pitcaria.models.cliente import Cliente
from pitcaria.models.pizzaria import Pizzaria

class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cliente
        fields = ('password', 'username',)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if Cliente.objects.filter(username=username).exists():
            username = Cliente.objects.get(username=username)
            if authenticate(username=username, password=password) is None:
                raise forms.ValidationError(("Usuario ou senha incorretos"))
        else:
            raise forms.ValidationError(("Usuário não existe"))
        return self.cleaned_data

