# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        self.result = self.app.get('/test')

        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), 'Rota de testes funcionando')


# https://www.lambdatest.com/learning-hub/pytest-tutorial