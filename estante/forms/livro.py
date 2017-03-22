# coding=utf-8
from django import forms
from estante.models import Livro
from datetime import date

class LivroForm(forms.ModelForm ):
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

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        if str.isalpha(str(autor)) == False:
            raise forms.ValidationError('Autor não pode conter números')
        else:
            return autor

    def clean_ano(self):
        ano = self.cleaned_data['ano']
        if ano >0 and ano < date.today().year:
            return ano
        else:
            raise forms.ValidationError('Data indisponivel')

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

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        if str.isalpha(str(autor)) == False:
            raise forms.ValidationError('Autor não pode conter números')
        else:
            return autor

    def clean_ano(self):
        ano = self.cleaned_data['ano']
        if ano >0 and ano < date.today().year:
            return ano
        else:
            raise forms.ValidationError('Data indisponivel')
