from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


segundos = 0


class Historia2(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_000_setup(self):
        driver = setup_selenium()
        for i in range(2):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="registro")

            usuario.send_keys(f"Teste2{i}")
            nome_usuario.send_keys(f"Marcílio{i}")
            email.send_keys(f"hist2{i}@teste.com")
            senha.send_keys("Teste12345")
            time.sleep(segundos)
            botao.send_keys(Keys.ENTER)

            if i == 1:
                time.sleep(segundos)
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
                nome_loja.send_keys("Logrec")
                imgperfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                imgbanner.send_keys("https://i.imgur.com/T2umQUo.jpeg")
                descloja.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
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

        usuario.send_keys("Teste21")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        time.sleep(segundos)
        driver.get("http://127.0.0.1:8000/add_produto")
        foto = driver.find_element(by=By.NAME, value="foto1")
        prod = driver.find_element(by=By.NAME, value="nome_produto")
        descricao = driver.find_element(by=By.NAME, value="descricao")
        preco = driver.find_element(by=By.NAME, value="preco")
        qntd = driver.find_element(by=By.NAME, value="qntd")
        categoria = driver.find_element(by=By.NAME, value="select")
        categoria = Select(categoria)
        enviar = driver.find_element(by=By.NAME, value="Add")

        foto.send_keys("https://static22.minhalojanouol.com.br/brofistloja/produto/20210701161644_6137993863_D.jpg")
        prod.send_keys("Charizard 1999 - 1° Edição")
        descricao.send_keys("Carta Charizard 1999 - 1° Edição")
        preco.send_keys("1700000")
        qntd.send_keys("1")
        categoria.select_by_visible_text("Cartas")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        self.assertEquals(
            driver.find_element(by=By.TAG_NAME, value="h5").text,
            "Charizard 1999 - 1° Edição"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def test_002_cenario2(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste21")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        time.sleep(segundos)
        driver.get("http://127.0.0.1:8000/add_produto")
        foto = driver.find_element(by=By.NAME, value="foto1")
        prod = driver.find_element(by=By.NAME, value="nome_produto")
        descricao = driver.find_element(by=By.NAME, value="descricao")
        preco = driver.find_element(by=By.NAME, value="preco")
        qntd = driver.find_element(by=By.NAME, value="qntd")
        enviar = driver.find_element(by=By.NAME, value="Add")

        foto.send_keys("https://i.ebayimg.com/images/g/HbYAAOSwKeVjOsBa/s-l1600.jpg")
        prod.send_keys("Black Lotus - Beta")
        descricao.send_keys("Black Lotus - Beta, uma das cartas mais raras do Magic")
        preco.send_keys("4039553")
        qntd.send_keys("1")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        time.sleep(segundos)
        minhaloja = driver.find_element(by=By.NAME, value="MLoja")
        minhaloja.click()

        self.assertEquals(
            driver.find_element(by=By.TAG_NAME, value="h5").text,
            "Charizard 1999 - 1° Edição"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def teste_002_cenario3(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste20")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        time.sleep(segundos)
        driver.get("http://127.0.0.1:8000/add_produto")
        self.assertEquals(
            driver.title,
            "Login"
        )