# coding=utf-8

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import authenticate
from django.forms.extras import SelectDateWidget
from django.forms.fields import DateField
import datetime


from pitcaria.models.cliente import Cliente


class ClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=254, label='Nome de Usuário')
    first_name = forms.CharField(max_length=40, label='Nome')
    last_name = forms.CharField(max_length=40, label='Sobrenome')
    cpf = forms.CharField(label='CPF')
    telefone = forms.IntegerField(label='Telefone')
    password = forms.CharField(widget=forms.PasswordInput())
    data_nascimento = DateField(widget=SelectDateWidget(years=range(1900, 2016),
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)

    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['date_joined', 'is_active']

    def save(self, commit=True):
        cliente = super(ClienteForm, self).save(commit=False)
        if cliente.data_nascimento > datetime.date.today():
            raise forms.ValidationError('Data indisponivel')
        if commit:
            cliente.save()
        return cliente

    def clean(self):
        try:
            nome = self.cleaned_data['first_name']
            if nome == "":
                msg = "Este campo é obrigatório."
                self._errors['first_name'] = self.error_class([msg])

            for digito in nome:
                if digito.isdecimal():
                    msg = "Nome deve conter apenas letras."
                    self._errors['first_name'] = self.error_class([msg])
        except Exception:
            print 'excpet'
            msg = 'Este campo é obrigatório.'
            self._errors['first_name'] = self.error_class([msg])

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        for digito in cpf:
            if not digito.isdecimal():
                raise forms.ValidationError("CPF deve conter somente números.")
        if Cliente.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Esse CPF já existe.")
        if len(cpf) != 11:
            raise forms.ValidationError("CPF possui exatamente 11 digítos.")
        d1 = 0
        d2 = 0
        i = 0
        while i < 10:
            d1, d2, i = (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1, (
                d2 + (int(cpf[i]) * (11 - i))) % 11, i + 1
        if not ((int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11 - d2 if d2 > 1 else 0))):
            raise forms.ValidationError("CPF inválido")
        return cpf

    def clean_data_nascimento(self):
        data = self.cleaned_data['data_nascimento']
        if data.year > 2016:
            raise forms.ValidationError("Data acima da atual")
        if data.year < 1900:
            raise forms.ValidationError("Tem certeza de que você está vivo?")
        return data

    def clean_password(self):
        senha = self.cleaned_data['password']
        if len(senha) < 7:
            raise forms.ValidationError("Senha tem que ter ao menos 8 caracteres")
        return senha





