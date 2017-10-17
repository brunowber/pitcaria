# coding: utf-8
import os
import django
import sys

sys.path.append("D:\Faculdade\Projetos_Pycharm\pitcaria\>")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")

django.setup()


def populate():
    add_cliente("brunoweber", "bruno1234", "Bruno", "weber", "09741044933", "4799369233", "1997-03-26")


def add_cliente(user, senha, nome, sobrenome, cpf, telefone, nasc):
    from pitcaria.models import Cliente
    # try:
    v = Cliente.objects.get_or_create(username=user, password=senha, first_name=nome, last_name=sobrenome,
                                             cpf=cpf, telefone=telefone, data_nascimento=nasc, nota=0)[0]
    v.save()
    # except:
    #   print ("Está faltando dados")


populate()
