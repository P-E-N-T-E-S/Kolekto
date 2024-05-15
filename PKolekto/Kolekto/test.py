from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

class Historia1(LiveServerTestCase):

    def test_cenario1(self):
        #Dado
        driver.get("http://127.0.0.1:8000/registro")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome_usuario = driver.find_element(by=By.NAME, value="nome")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="senha")
        botao = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys(f"Teste4")
        nome_usuario.send_keys(f"João")
        email.send_keys(f"hist4@teste.com")
        senha.send_keys("Teste12345")
        botao.send_keys(Keys.ENTER)
        #Quando
        driver.get("http://127.0.0.1:8000/nova_loja")
        perfil = driver.find_element(by=By.ID, value="perfil")
        nascimento = driver.find_element(by=By.ID, value="nascimento")
        cpf = driver.find_element(by=By.ID, value="cpf")
        nome_loja = driver.find_element(by=By.ID, value="nome_loja")
        descricao = driver.find_element(by=By.ID, value="descricao")
        rua = driver.find_element(by=By.ID, value="RuaAvenida")
        botao = driver.find_element(by=By.ID, value="cadastro")
        estado = driver.find_element(by=By.ID, value="estado")
        estado = Select(estado)

        nascimento.send_keys("29082003")
        rua.send_keys("Rua dos bobos")
        cpf.send_keys("164.718.030-95")
        nome_loja.send_keys("Minis Recife")
        perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
        descricao.send_keys(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        estado.select_by_visible_text("Pernambuco")
        botao.send_keys(Keys.ENTER)
        #Entao
        
        driver.get("http://127.0.0.1:8000/minha_loja")

        self.assertEqual(
        driver.find_element(by=By.NAME, value="tituloLoja").text,
        "Minis Recife"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def test_cenario2(self):
        #Dado
        driver.get("http://127.0.0.1:8000/registro")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome_usuario = driver.find_element(by=By.NAME, value="nome")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="senha")
        botao = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys(f"Teste40")
        nome_usuario.send_keys(f"João")
        email.send_keys(f"hist41@teste.com")
        senha.send_keys("Teste12345")
        botao.send_keys(Keys.ENTER)
        
        driver.get("http://127.0.0.1:8000/nova_loja")
        perfil = driver.find_element(by=By.ID, value="perfil")
        nascimento = driver.find_element(by=By.ID, value="nascimento")
        cpf = driver.find_element(by=By.ID, value="cpf")
        nome_loja = driver.find_element(by=By.ID, value="nome_loja")
        descricao = driver.find_element(by=By.ID, value="descricao")
        rua = driver.find_element(by=By.ID, value="RuaAvenida")
        botao = driver.find_element(by=By.ID, value="cadastro")
        estado = driver.find_element(by=By.ID, value="estado")
        estado = Select(estado)

        nascimento.send_keys("29082003")
        rua.send_keys("Rua dos bobos")
        cpf.send_keys("164.718.030-95")
        nome_loja.send_keys("Gêmeos das Minis")
        perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
        descricao.send_keys(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        estado.select_by_visible_text("Pernambuco")
        botao.send_keys(Keys.ENTER)
        
        driver.get("http://127.0.0.1:8000/logout")
        
        driver.get("http://127.0.0.1:8000/registro")
        usuario = driver.find_element(by=By.NAME, value="username")
        nome_usuario = driver.find_element(by=By.NAME, value="nome")
        email = driver.find_element(by=By.NAME, value="email")
        senha = driver.find_element(by=By.NAME, value="senha")
        botao = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys(f"Teste42")
        nome_usuario.send_keys(f"João")
        email.send_keys(f"hist42@teste.com")
        senha.send_keys("Teste12345")
        botao.send_keys(Keys.ENTER)

        #Quando

        driver.get("http://127.0.0.1:8000/nova_loja")
        perfil = driver.find_element(by=By.ID, value="perfil")
        nascimento = driver.find_element(by=By.ID, value="nascimento")
        cpf = driver.find_element(by=By.ID, value="cpf")
        nome_loja = driver.find_element(by=By.ID, value="nome_loja")
        descricao = driver.find_element(by=By.ID, value="descricao")
        rua = driver.find_element(by=By.ID, value="RuaAvenida")
        botao = driver.find_element(by=By.ID, value="cadastro")
        estado = driver.find_element(by=By.ID, value="estado")
        estado = Select(estado)

        nascimento.send_keys("29082003")
        rua.send_keys("Rua dos bobos")
        cpf.send_keys("164.718.030-95")
        nome_loja.send_keys("Gêmeos das Minis")
        perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
        descricao.send_keys(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        estado.select_by_visible_text("Pernambuco")
        botao.send_keys(Keys.ENTER)

        #Entao

        self.assertEqual(
            driver.find_element(by=By.ID, value="erros").text,
            "Já existe uma loja com esse nome."
        )
        driver.get("http://127.0.0.1:8000/logout")
     
    