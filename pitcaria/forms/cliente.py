# coding=utf-8

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import authenticate
from django.forms.extras import SelectDateWidget
from django.forms.fields import DateField

from pitcaria.models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=254, label='Nome de Usuário')
    first_name = forms.CharField(max_length=40, label='Nome')
    last_name = forms.CharField(max_length=40, label='Sobrenome')
    cpf = forms.CharField(label='CPF')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())
    data_nascimento = DateField(
    widget=SelectDateWidget(years=range(1900, 2100),
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)

    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['date_joined', 'nota', 'is_active']


class ClienteEditForm(forms.ModelForm):
    first_name=forms.CharField(max_length=40, label='Nome')
    last_name=forms.CharField(max_length=40, label='Sobrenome')
    cpf = forms.IntegerField(label='CPF')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())
    data_nascimento = forms.DateField()

    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['date_joined', 'username', 'is_active', 'nota']


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
            if authenticate(username=username, password=password) is None:
                raise forms.ValidationError(("Usuario ou senha incorretos"))
        return self.cleaned_data

