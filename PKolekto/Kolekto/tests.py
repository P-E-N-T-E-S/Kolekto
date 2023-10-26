from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

class Historia4(LiveServerTestCase):
    def test_000_setup(self):
        listloja = ['', '', 'Gêmeos das Minis', 'Brinquedos do Futuro']
        for i in range(4):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="registro")

            usuario.send_keys(f"Teste{i}")
            nome_usuario.send_keys(f"João{i}")
            email.send_keys(f"teste{i}@teste.com")
            senha.send_keys("Teste12345")
            botao.click()

            if i >= 2:
                driver.get("http://127.0.0.1:8000/nova_loja")
                nascimento = driver.find_element(by=By.NAME, value="nascimento")
                cidade = driver.find_element(by=By.NAME, value="cidade")
                cpf = driver.find_element(by=By.NAME, value="cpf")
                nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
                imgperfil = driver.find_element(by=By.NAME, value="perfil")
                imgbanner = driver.find_element(by=By.NAME, value="banner")
                descloja = driver.find_element(by=By.NAME, value="descricao")
                time.sleep(2)
                enviar = driver.find_element(by=By.NAME, value="criar")

                nascimento.send_keys("29082003")
                cidade.send_keys("Rio Branco")
                cpf.send_keys("000.000.000-00")
                nome_loja.send_keys(listloja[i])
                imgperfil.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
                imgbanner.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
                descloja.send_keys("lorem impsum etc e talz")
                time.sleep(2)
                enviar.click()

        driver.get("http://127.0.0.1:8000/logout/")


    def test_001_cenario1(self):
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="logar")

        usuario.send_keys("Teste0")
        senha.send_keys("Teste12345")
        enviar.click()

        driver.get("http://127.0.0.1:8000/nova_loja")
        nascimento = driver.find_element(by=By.NAME, value="nascimento")
        cidade = driver.find_element(by=By.NAME, value="cidade")
        cpf = driver.find_element(by=By.NAME, value="cpf")
        nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
        imgperfil = driver.find_element(by=By.NAME, value="perfil")
        imgbanner = driver.find_element(by=By.NAME, value="banner")
        descloja = driver.find_element(by=By.NAME, value="descricao")
        time.sleep(2)
        enviar = driver.find_element(by=By.NAME, value="criar")

        nascimento.send_keys("29082003")
        cidade.send_keys("Rio Branco")
        cpf.send_keys("000.000.000-00")
        nome_loja.send_keys("Minis Recife")
        imgperfil.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
        imgbanner.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
        descloja.send_keys("lorem impsum etc e talz")
        time.sleep(2)
        enviar.click()

        minhaloja = driver.find_element(by=By.NAME, value="MLoja")
        minhaloja.click()

        self.assertEquals(
            driver.find_element(by=By.NAME, value="tituloLoja")
        )




