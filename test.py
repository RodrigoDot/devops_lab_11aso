# -*- coding: utf-8 -*-
from app import app
import unittest

from selenium.webdriver.common.by import By
import sys

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    # def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        # self.assertEqual(self.result.data.decode('utf-8'), "Rodrigo")


    # def test_item(self, driver):
    #    driver.get('/')
    #    sample_text = "Rodrigo"
    #    text_field = driver.find_element(By.ID, "sampletodotext")
    #    email_text_field.send_keys(sample_text)


    #    driver.find_element(By.ID, "addbutton").click()