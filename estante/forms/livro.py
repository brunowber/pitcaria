# coding=utf-8
from django import forms

class LivroForm(forms.Form):
    id_livro = forms.IntegerField(max_value=15, label='ISBN')
    titulo = forms.CharField(max_length=100, label='Título')
    autor = forms.CharField(max_length=50, label='Autor')
    editora = forms.CharField(max_length=50, label='Editora')
    ano = forms.IntegerField(max_value=4, label='Ano')
