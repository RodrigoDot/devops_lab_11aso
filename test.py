# -*- coding: utf-8 -*-
# import pytest
# from selenium.webdriver.common.by import By
# import sys

from app import app
import unittest

# @pytest.mark.usefixtures('driver')
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
        # verifica o retorno do conteudo da pagina
        print('PRINT >>>>>>>>>>', self.result.data.decode('utf-8'))

        HtmlFile = open('templates/index.html', 'r', encoding='utf-8')
        source_code = HtmlFile.read() 

        print('source_code >>>>>>>>>>', source_code)

        self.assertEqual(self.result.data.decode('utf-8'), source_code)


    # def test_content(self):
    #     driver_node = webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver=driver_node
    #     self.driver.maximize_window()

    #     self.driver.get('/')
    #     self.driver.implicitly_wait(10)

    #     title1_text = "Rodrigo"
    #     text_title1 = driver.find_element(By.ID, "title1")
    #     text_title1.send_keys(title1_text)

    #     assert text_title1 == title1_text

    #     title2_text = "Barbosa"
    #     text_title2 = driver.find_element(By.ID, "title2")
    #     text_title2.send_keys(title2_text)

    #     assert text_title2 == title2_text

    #     title3_text = "Costa"
    #     text_field3 = driver.find_element(By.ID, "title3")
    #     text_field3.send_keys(title3_text)

    #     assert text_field3 == title3_text

# https://www.lambdatest.com/learning-hub/pytest-tutorial