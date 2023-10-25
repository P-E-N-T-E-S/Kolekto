'''import pathlib
from django.contrib.auth.models import User
import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .models import Loja
from selenium.webdriver.common.by import By

# Create your tests here.

#http://127.0.0.1:8000/

class Historia4(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()
    def __init__(self):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=servico)

    def setUp(self):
        userhist1 = User.objects.create_user(username="Teste", password="Testando", email="teste@teste.com", first_name="Teste")
        userhist2 = User.objects.create_user(username="Teste2", password="Testando2", email="teste2@teste.com", first_name="Teste2")

    def cenario1(self):
        Banner="https://i.imgur.com/7d4psY9.jpeg"
        Perfil = "https://i.imgur.com/Uschheg.jpeg"
        NomeLoja = "Minis Recife"
        cpf = "000.000.000-00"
        datanascimento = "01/01/2000"
        estado = "PE"
        cidade = "Recife"
        descricao = "Lorem Ipsun etc e talz"

        usuario = "Teste"
        senha = "Testando"

        navegador.get("http://127.0.0.1:8000/login")
        loginbox = navegador.find_element(by=By.NAME, value="username")
        senhabox = navegador.find_element(by=By.NAME, value="senha")
        botaosubmit = navegador.find_element(by=By.CSS_SELECTOR, value="button")

        loginbox.send_keys(usuario)
        senhabox.send_keys(senha)
        botaosubmit.click()'''

