# coding: utf-8
import os
import django
import sys

sys.path.append("D:\Faculdade\Projetos_Pycharm\pitcaria\>")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")

django.setup()


def populate():
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044933", "4799369233", "1997-03-26") #Caso de sucesso
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044933", "4799369233", "2019-03-26") #Data acima da atual arrumar
    # add_cliente("brunoweber", "", "Bruno", "Weber", "09741044933", "4799369233", "1997-03-26") #Senha em branco
    # add_cliente("brunoweber", "bruno1234", "", "Weber", "09741044933", "4799369233", "1997-03-26") #Primeiro nome em branco
    # add_cliente("brunoweber", "bruno1234", "Bruno", "", "09741044933", "4799369233", "1997-03-26") #Ultimo nome em branco
    add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "", "4799369233", "1997-03-26")  # CPF em branco
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044933", "", "1997-03-26") #Telefone em branco
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044933", "4799369233", "") #Data nascimento nome em branco
    # add_cliente("brunoweber", "bruno1234", "Bruno1234", "Weber1234", "09741044933", "4799369233", "1997-03-26") #Nome e sobrenome com numeros
    # add_cliente("brunoweber", "bru", "Bruno", "Weber", "0974104493", "4799369233", "1997-03-26") #Senha com menos de 8 digitos
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044933", "99369233", "1997-03-26") #Telefone sem DDD
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044931", "4799369233", "1997-03-26") #CPF invalido
    # add_cliente("brunoweber", "bruno1234", "Bruno", "Weber", "09741044933", "4799369233", "1700-03-26") #Data muito abaixo da atual
    # add_cliente("bru", "bruno1234", "Bruno", "Weber", "09741044933", "4799369233", "1997-03-26") #Username com menos de 8 digitos


def add_cliente(user, senha, nome, sobrenome, cpf, telefone, nasc):
    from pitcaria.models import Cliente
    from pitcaria.forms import ClienteForm

    form = ClienteForm(username=user)
    print form
    # if form.is_valid():
    try:
        v = Cliente.objects.get_or_create(username=user, password=senha, first_name=nome, last_name=sobrenome,
                                          cpf=cpf, telefone=telefone, data_nascimento=nasc, nota=0)[0]
        v.save()
        print("Conta cadastrada com sucesso")
    except Exception, e:
        print e
    print ("Está faltando dados")
    # else:
    print "Está faltando dados"


populate()
