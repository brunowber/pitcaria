# -*- coding: utf-8 -*-
import unittest


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        from pitcaria.forms import ClienteForm
        cliente1 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                    'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': '1997-03-26'}
        self.form1 = ClienteForm(data=cliente1)

        cliente2 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                    'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': '2019-03-26'}
        self.form2 = ClienteForm(data=cliente2)

        cliente3 = {'username': 'brunoweber', 'password': '', 'first_name': 'Bruno',
                    'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': '1997-03-26'}
        self.form3 = ClienteForm(data=cliente3)

        cliente4 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': '',
                    'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': '1997-03-26'}
        self.form4 = ClienteForm(data=cliente4)

        cliente5 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                    'last_name': '', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': '1997-03-26'}
        self.form5 = ClienteForm(data=cliente5)

        cliente6 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                    'last_name': 'Weber', 'cpf': '', 'telefone': '4734324161',
                    'data_nascimento': '1997-03-26'}
        self.form6 = ClienteForm(data=cliente6)

        cliente7 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                    'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '',
                    'data_nascimento': '1997-03-26'}
        self.form7 = ClienteForm(data=cliente7)

        cliente8 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                    'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': ''}
        self.form8 = ClienteForm(data=cliente8)

        cliente9 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno123',
                    'last_name': 'Weber123', 'cpf': '09741044933', 'telefone': '4734324161',
                    'data_nascimento': '1997-03-26'}
        self.form9 = ClienteForm(data=cliente9)

        cliente10 = {'username': 'brunoweber', 'password': 'bru', 'first_name': 'Bruno',
                     'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                     'data_nascimento': '1997-03-26'}
        self.form10 = ClienteForm(data=cliente10)

        cliente11 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                     'last_name': 'Weber', 'cpf': '0974104493', 'telefone': '4734324161',
                     'data_nascimento': '1997-03-26'}
        self.form11 = ClienteForm(data=cliente11)

        cliente13 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                     'last_name': 'Weber', 'cpf': '09741044932', 'telefone': '4734324161',
                     'data_nascimento': '1997-03-26'}
        self.form13 = ClienteForm(data=cliente13)

        cliente14 = {'username': 'brunoweber', 'password': 'bruno1234', 'first_name': 'Bruno',
                     'last_name': 'Weber', 'cpf': '09741044933', 'telefone': '4734324161',
                     'data_nascimento': '1700-03-26'}
        self.form14 = ClienteForm(data=cliente14)

    def test(self):
        self.assertEquals(self.form1.is_valid(), True)  # Todos os dados
        self.assertEquals(self.form2.is_valid(), False)  # Data acima da atual
        self.assertEquals(self.form3.is_valid(), False)  # Sem senha
        self.assertEquals(self.form4.is_valid(), False)  # Sem nome
        self.assertEquals(self.form5.is_valid(), False)  # Sem sobrenome
        self.assertEquals(self.form6.is_valid(), False)  # Sem CPF
        self.assertEquals(self.form7.is_valid(), False)  # Sem Telefone
        self.assertEquals(self.form8.is_valid(), False)  # Sem Data_nascimento
        self.assertEquals(self.form9.is_valid(), False)  # Nome ou sobrenome não possuem numeros
        self.assertEquals(self.form10.is_valid(), False)  # Senha deve conter ao menos 8 caracteres
        self.assertEquals(self.form11.is_valid(), False)  # CPF deve conter exatamente 12 caracteres
        self.assertEquals(self.form13.is_valid(), False)  # Esse cpf não existe
        self.assertEquals(self.form14.is_valid(), False)  # Data muito abaixo da atual
