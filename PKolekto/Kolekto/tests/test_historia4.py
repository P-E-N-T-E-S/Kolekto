from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


segundos = 0


class Historia4(LiveServerTestCase):


    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_000_setup(self):
        driver = setup_selenium()
        listloja = ['', '', 'Gêmeos das Minis', 'Brinquedos do Futuro']
        for i in range(4):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="registro")

            usuario.send_keys(f"Teste4{i}")
            nome_usuario.send_keys(f"João{i}")
            email.send_keys(f"hist4{i}@teste.com")
            senha.send_keys("Teste12345")
            botao.send_keys(Keys.ENTER)

            if i >= 2:
                driver.get("http://127.0.0.1:8000/nova_loja")
                nascimento = driver.find_element(by=By.NAME, value="nascimento")
                cidade = driver.find_element(by=By.NAME, value="cidade")
                cpf = driver.find_element(by=By.NAME, value="cpf")
                nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
                imgperfil = driver.find_element(by=By.NAME, value="perfil")
                imgbanner = driver.find_element(by=By.NAME, value="banner")
                descloja = driver.find_element(by=By.NAME, value="descricao")
                enviar = driver.find_element(by=By.NAME, value="criar")

                nascimento.send_keys("29082003")
                cidade.send_keys("Rio Branco")
                cpf.send_keys("000.000.000-00")
                nome_loja.send_keys(listloja[i])
                imgperfil.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
                imgbanner.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
                descloja.send_keys("lorem impsum etc e talz")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)
        self.assertTrue(
            True
        )
        driver.get("http://127.0.0.1:8000/logout/")

    def test_001_cenario1(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste40")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/nova_loja")
        nascimento = driver.find_element(by=By.NAME, value="nascimento")
        cidade = driver.find_element(by=By.NAME, value="cidade")
        cpf = driver.find_element(by=By.NAME, value="cpf")
        nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
        imgperfil = driver.find_element(by=By.NAME, value="perfil")
        imgbanner = driver.find_element(by=By.NAME, value="banner")
        descloja = driver.find_element(by=By.NAME, value="descricao")
        time.sleep(segundos)
        enviar = driver.find_element(by=By.NAME, value="criar")

        nascimento.send_keys("29082003")
        cidade.send_keys("Rio Branco")
        cpf.send_keys("000.000.000-00")
        nome_loja.send_keys("Minis Recife")
        imgperfil.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
        imgbanner.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
        descloja.send_keys("lorem impsum etc e talz")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        time.sleep(segundos)
        minhaloja = driver.find_element(by=By.NAME, value="MLoja")
        minhaloja.click()

        self.assertEquals(
            driver.find_element(by=By.NAME, value="tituloLoja").text,
            "Minis Recife"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def test_002_cenario2(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste41")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/nova_loja")
        nascimento = driver.find_element(by=By.NAME, value="nascimento")
        cidade = driver.find_element(by=By.NAME, value="cidade")
        cpf = driver.find_element(by=By.NAME, value="cpf")
        nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
        imgperfil = driver.find_element(by=By.NAME, value="perfil")
        imgbanner = driver.find_element(by=By.NAME, value="banner")
        descloja = driver.find_element(by=By.NAME, value="descricao")
        enviar = driver.find_element(by=By.NAME, value="criar")

        nascimento.send_keys("29082003")
        cidade.send_keys("Rio Branco")
        cpf.send_keys("000.000.000-00")
        nome_loja.send_keys("Gêmeos das Minis")
        imgperfil.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
        imgbanner.send_keys("https://i.imgur.com/6K0TQwo.jpeg")
        descloja.send_keys("lorem impsum etc e talz")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        self.assertEquals(
            driver.find_element(by=By.XPATH, value="/html/body/main/div/form/p").text,
            "Já existe uma loja com esse nome."
        )
        driver.get("http://127.0.0.1:8000/logout")

    def teste_003_cenario3(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/nova_loja")
        self.assertEquals(
            driver.title,
            "Kolekto: Login"
        )

    def teste_004_cenario4(self):
        driver = setup_selenium()
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
        enviar = driver.find_element(by=By.NAME, value="criar")

        nascimento.send_keys("29082003")

        nome_loja.send_keys(Keys.CONTROL + 'a')
        nome_loja.send_keys("Estatuetas 10")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        self.assertEquals(
            driver.find_element(by=By.NAME, value="tituloLoja").text,
            "Estatuetas 10"
        )
