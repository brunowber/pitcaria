# coding=utf-8


from estante.forms.validators.livro_validator import *
from django import forms
from estante.models import Livro


class LivroForm(forms.ModelForm):
    id_livro = forms.IntegerField(label='ISBN')
    titulo = forms.CharField(max_length=50, label='Título')
    autor = forms.CharField(max_length=50, label='Autor')
    editora = forms.CharField(max_length=50, label='Editora')
    ano = forms.IntegerField(label='Ano')

    class Meta:
        model = Livro
        fields = "__all__"
        exclude = ("dono",)

    def clean_status(self):
        status = True
        return status

    def clean_id_livro(self):
        id_livro = self.cleaned_data['id_livro']
        livro =Livro.objects.filter(id_livro__contains=id_livro).exists()
        if livro:
            raise forms.ValidationError('ISBN já utilizado')
        if len(str(id_livro)) !=13:
            raise forms.ValidationError('ISBN precisa de 13 digitos')
        else:
            return id_livro

    def clean_ano(self):
        return AnoValidator(self.cleaned_data['ano'])


class LivroEditaForm(forms.ModelForm ):
    titulo = forms.CharField(max_length=50, label='Título')
    autor = forms.CharField(max_length=50, label='Autor')
    editora = forms.CharField(max_length=50, label='Editora')
    ano = forms.IntegerField(label='Ano')

    class Meta:
        model = Livro
        fields = "__all__"
        exclude = ("dono","id_livro",)

    def clean_status(self):
        status = True
        return status

    def clean_ano(self):
        return AnoValidator(self.cleaned_data['ano'])
