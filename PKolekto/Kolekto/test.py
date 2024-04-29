from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class Historia1(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_cenario1(self):
        #Dado
        self.selenium.get(f"{self.live_server_url}/registro")
        usuario =self.selenium.find_element(by=By.NAME, value="username")
        nome_usuario = self.selenium.find_element(by=By.NAME, value="nome")
        email = self.selenium.find_element(by=By.NAME, value="email")
        senha = self.selenium.find_element(by=By.NAME, value="senha")
        botao = self.selenium.find_element(by=By.NAME, value="Logar")

        usuario.send_keys(f"Teste4")
        nome_usuario.send_keys(f"João")
        email.send_keys(f"hist4@teste.com")
        senha.send_keys("Teste12345")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        time.sleep(2)
         #Quando
        self.selenium.get(f"{self.live_server_url}/nova_loja")
        perfil = self.selenium.find_element(by=By.ID, value="perfil")
        nascimento = self.selenium.find_element(by=By.ID, value="nascimento")
        cpf = self.selenium.find_element(by=By.ID, value="cpf")
        nome_loja = self.selenium.find_element(by=By.ID, value="nome_loja")
        descricao = self.selenium.find_element(by=By.ID, value="descricao")
        rua = self.selenium.find_element(by=By.ID, value="RuaAvenida")
        botao = self.selenium.find_element(by=By.ID, value="cadastro")
        estado = self.selenium.find_element(by=By.ID, value="estado")
        estado = Select(estado)

        nascimento.send_keys("29082003")
        rua.send_keys("Rua dos bobos")
        cpf.send_keys("164.718.030-95")
        nome_loja.send_keys("Minis Recife")
        perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
        descricao.send_keys(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        estado.select_by_visible_text("Pernambuco")
        time.sleep(2)
        botao.send_keys(Keys.ENTER)
        time.sleep(2)
        #Entao
        
        self.selenium.get(f"{self.live_server_url}/minha_loja")
        time.sleep(5)

        self.assertEqual(
        self.selenium.find_element(by=By.NAME, value="tituloLoja").text,
        "Minis Recife"
        )
        self.selenium.get(f"{self.live_server_url}/logout")

    def test_cenario2(self):
        #Dado
        self.selenium.get(f"{self.live_server_url}/registro")
        usuario = self.selenium.find_element(by=By.NAME, value="username")
        nome_usuario = self.selenium.find_element(by=By.NAME, value="nome")
        email = self.selenium.find_element(by=By.NAME, value="email")
        senha = self.selenium.find_element(by=By.NAME, value="senha")
        botao = self.selenium.find_element(by=By.NAME, value="Logar")

        usuario.send_keys(f"Teste40")
        nome_usuario.send_keys(f"João")
        email.send_keys(f"hist41@teste.com")
        senha.send_keys("Teste12345")
        botao.send_keys(Keys.ENTER)
        
        self.selenium.get(f"{self.live_server_url}/nova_loja")
        perfil = self.selenium.find_element(by=By.ID, value="perfil")
        nascimento = self.selenium.find_element(by=By.ID, value="nascimento")
        cpf = self.selenium.find_element(by=By.ID, value="cpf")
        nome_loja = self.selenium.find_element(by=By.ID, value="nome_loja")
        descricao = self.selenium.find_element(by=By.ID, value="descricao")
        rua = self.selenium.find_element(by=By.ID, value="RuaAvenida")
        botao = self.selenium.find_element(by=By.ID, value="cadastro")
        estado = self.selenium.find_element(by=By.ID, value="estado")
        estado = Select(estado)

        nascimento.send_keys("29082003")
        rua.send_keys("Rua dos bobos")
        cpf.send_keys("164.718.030-95")
        nome_loja.send_keys("Gêmeos das Minis")
        perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
        descricao.send_keys(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        estado.select_by_visible_text("Pernambuco")
        time.sleep(1)
        botao.send_keys(Keys.ENTER)
        
        self.selenium.get(f"{self.live_server_url}/logout")
        
        self.selenium.get(f"{self.live_server_url}/registro")
        usuario = self.selenium.find_element(by=By.NAME, value="username")
        nome_usuario = self.selenium.find_element(by=By.NAME, value="nome")
        email = self.selenium.find_element(by=By.NAME, value="email")
        senha = self.selenium.find_element(by=By.NAME, value="senha")
        botao = self.selenium.find_element(by=By.NAME, value="Logar")

        usuario.send_keys(f"Teste42")
        nome_usuario.send_keys(f"João")
        email.send_keys(f"hist42@teste.com")
        senha.send_keys("Teste12345")
        botao.send_keys(Keys.ENTER)

        #Quando

        self.selenium.get(f"{self.live_server_url}/nova_loja")
        perfil = self.selenium.find_element(by=By.ID, value="perfil")
        nascimento = self.selenium.find_element(by=By.ID, value="nascimento")
        cpf = self.selenium.find_element(by=By.ID, value="cpf")
        nome_loja = self.selenium.find_element(by=By.ID, value="nome_loja")
        descricao = self.selenium.find_element(by=By.ID, value="descricao")
        rua = self.selenium.find_element(by=By.ID, value="RuaAvenida")
        botao = self.selenium.find_element(by=By.ID, value="cadastro")
        estado = self.selenium.find_element(by=By.ID, value="estado")
        estado = Select(estado)

        nascimento.send_keys("29082003")
        rua.send_keys("Rua dos bobos")
        cpf.send_keys("164.718.030-95")
        nome_loja.send_keys("Gêmeos das Minis")
        perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
        descricao.send_keys(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
        estado.select_by_visible_text("Pernambuco")
        time.sleep(1)
        botao.send_keys(Keys.ENTER)

        #Entao

        self.assertEqual(
            self.selenium.find_element(by=By.ID, value="erros").text,
            "Já existe uma loja com esse nome."
        )
        self.selenium.get(f"{self.live_server_url}/logout")
     
    