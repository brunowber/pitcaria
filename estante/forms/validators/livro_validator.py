# coding=utf-8
from datetime import date
from django.forms import forms


def AnoValidator(ano):
    if ano < 0 and ano > date.today().year:
        raise forms.ValidationError('Data indisponivel')
    else:
        return ano
