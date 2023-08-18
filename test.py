# -*- coding: utf-8 -*-
from app import app
import unittest
import pytest
from selenium.webdriver.common.by import By
import sys

@pytest.mark.usefixtures('driver')
class Test:
    # def setUp(self):
    #     # cria uma instância do unittest, precisa do nome "setUp"
    #     self.app = app.test_client()

    #     # envia uma requisicao GET para a URL
    #     self.result = self.app.get('/')

    # def test_requisicao(self):
    #     # compara o status da requisicao (precisa ser igual a 200)
    #     self.assertEqual(self.result.status_code, 200)

    # def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        # self.assertEqual(self.result.data.decode('utf-8'), "Rodrigo")


    def test_item(self, driver):
       driver.get('/')
       title1_text = "Rodrigo"
       text_title1 = driver.find_element(By.ID, "title1")
       text_title1.send_keys(title1_text)

       title2_text = "Barbosa"
       text_title2 = driver.find_element(By.ID, "title2")
       text_title2.send_keys(title2_text)

       title3_text = "Costa"
       text_field3 = driver.find_element(By.ID, "title3")
       text_field3.send_keys(title3_text)