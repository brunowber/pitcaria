# -*- coding: utf-8 -*-
import unittest


class HttpTestCase(unittest.TestCase):
    def setUp(self):
        from django.test.client import Client
        c = Client()
        self.response = c.get('/')
        self.response2 = c.get('/oipessoal')
        self.response3 = c.get('/home/')

    def test(self):
        self.assertEquals(self.response.status_code, 200)  # Menu inicial
        self.assertEquals(self.response2.status_code, 404)  # Link inexistente
        self.assertEquals(self.response3.status_code, 404)  # Link inexistente
