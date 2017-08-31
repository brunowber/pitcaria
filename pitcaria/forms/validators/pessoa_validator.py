# coding=utf-8
from django.forms import forms
from pitcaria.models import Cliente


def UsernameValidator(pessoa):
    if Pessoa.objects.filter(username=pessoa).exists():
        username = Pessoa.objects.get(username=pessoa)
        print (username)
    else:
        raise forms.ValidationError('Usuário não existe')
    return username

def CpfValidator(cpf):
    if len(str(cpf)) == 11:
        return cpf
    else:
        raise forms.ValidationError("CPF deve conter 11 dígitos!")

def NameValidator(nome):
    if nome.isalpha():
        return nome
    else:
        raise forms.ValidationError('Nome não pode conter números')