from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


segundos = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1440,1080")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)


class Historia04(LiveServerTestCase):

    def test_000_setup(self):
        listloja = ['', '', 'Gêmeos das Minis', 'Brinquedos do Futuro']
        for i in range(4):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="Logar")

            usuario.send_keys(f"Teste4{i}")
            nome_usuario.send_keys(f"João{i}")
            email.send_keys(f"hist4{i}@teste.com")
            senha.send_keys("Teste12345")
            botao.send_keys(Keys.ENTER)

            if i >= 2:
                driver.get("http://127.0.0.1:8000/nova_loja")
                perfil = driver.find_element(by=By.ID, value="perfil")
                nascimento = driver.find_element(by=By.ID, value="nascimento")
                cpf = driver.find_element(by=By.ID, value="cpf")
                nome_loja = driver.find_element(by=By.ID, value="nome_loja")
                descricao = driver.find_element(by=By.ID, value="descricao")
                rua = driver.find_element(by=By.ID, value="Rua/Avenida")
                botao = driver.find_element(by=By.ID, value="cadastro")
                estado = driver.find_element(by=By.ID, value="estado")
                estado = Select(estado)

                nascimento.send_keys("29082003")
                rua.send_keys("Rua dos bobos")
                cpf.send_keys("164.718.030-95")
                nome_loja.send_keys(listloja[i])
                perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                descricao.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                estado.select_by_visible_text("Pernambuco")
                time.sleep(segundos)
                botao.click()
        self.assertTrue(
            True
        )
        driver.get("http://127.0.0.1:8000/logout/")

    def test_001_cenario1(self):
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste40")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/nova_loja")
        perfil = driver.find_element(by=By.ID, value="perfil")
        nascimento = driver.find_element(by=By.ID, value="nascimento")
        cpf = driver.find_element(by=By.ID, value="cpf")
        nome_loja = driver.find_element(by=By.ID, value="nome_loja")
        descricao = driver.find_element(by=By.ID, value="descricao")
        rua = driver.find_element(by=By.ID, value="Rua/Avenida")
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
        time.sleep(segundos)
        botao.click()

        time.sleep(segundos)
        minhaloja = driver.find_element(by=By.NAME, value="MLoja")
        minhaloja.click()

        self.assertEqual(
            driver.find_element(by=By.NAME, value="tituloLoja").text,
            "Minis Recife"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def test_002_cenario2(self):
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste41")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/nova_loja")
        perfil = driver.find_element(by=By.ID, value="perfil")
        nascimento = driver.find_element(by=By.ID, value="nascimento")
        cpf = driver.find_element(by=By.ID, value="cpf")
        nome_loja = driver.find_element(by=By.ID, value="nome_loja")
        descricao = driver.find_element(by=By.ID, value="descricao")
        rua = driver.find_element(by=By.ID, value="Rua/Avenida")
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
        time.sleep(segundos)
        botao.click()

        self.assertEqual(
            driver.find_element(by=By.ID, value="erros").text,
            "Já existe uma loja com esse nome."
        )
        driver.get("http://127.0.0.1:8000/logout")

    def teste_003_cenario3(self):
        driver.get("http://127.0.0.1:8000/nova_loja")
        self.assertEqual(
            driver.title,
            "Kolekto: Login"
        )

    def teste_004_cenario4(self):
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste43")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get('http://127.0.0.1:8000/minha_loja')

        driver.find_element(by=By.ID, value="Editar").click()

        nascimento = driver.find_element(by=By.ID, value="nascimento")
        nome_loja = driver.find_element(by=By.ID, value="nome_loja")
        enviar = driver.find_element(by=By.ID, value="Alterar")

        nascimento.send_keys("29082003")

        nome_loja.send_keys(Keys.CONTROL + 'a')
        nome_loja.send_keys("Estatuetas 10")
        time.sleep(segundos)
        enviar.click()

        self.assertEqual(
            driver.find_element(by=By.NAME, value="tituloLoja").text,
            "Estatuetas 10"
        )
