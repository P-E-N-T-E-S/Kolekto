from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

segundos = 0


class Historia5(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_000_setup(self):
        driver = setup_selenium()
        for i in range(4):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="registro")

            usuario.send_keys(f"Teste5{i}")
            nome_usuario.send_keys(f"Thomaz{i}")
            email.send_keys(f"hist5{i}@teste.com")
            senha.send_keys("Teste12345")
            botao.send_keys(Keys.ENTER)

            if i == 1:
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
                nome_loja.send_keys("Minis Recife")
                imgperfil.send_keys("https://i.imgur.com/bXZHIgO.jpeg")
                imgbanner.send_keys("https://i.imgur.com/qbLig65.jpeg")
                descloja.send_keys("lorem impsum etc e talz")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

                driver.get("http://127.0.0.1:8000/add_produto")
                foto = driver.find_element(by=By.NAME, value="foto1")
                prod = driver.find_element(by=By.NAME, value="nome_produto")
                descricao = driver.find_element(by=By.NAME, value="descricao")
                preco = driver.find_element(by=By.NAME, value="preco")
                qntd = driver.find_element(by=By.NAME, value="qntd")
                enviar = driver.find_element(by=By.NAME, value="Add")
                categoria = driver.find_element(by=By.NAME, value="select")
                categoria = Select(categoria)

                categoria.select_by_visible_text("Cartas")
                foto.send_keys("https://i.imgur.com/10WPEMV.jpeg")
                prod.send_keys("Carta Pokemon: Charmander")
                descricao.send_keys("Charmander")
                preco.send_keys("10")
                qntd.send_keys("5")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

                driver.get("http://127.0.0.1:8000/add_produto")
                foto = driver.find_element(by=By.NAME, value="foto1")
                prod = driver.find_element(by=By.NAME, value="nome_produto")
                descricao = driver.find_element(by=By.NAME, value="descricao")
                preco = driver.find_element(by=By.NAME, value="preco")
                qntd = driver.find_element(by=By.NAME, value="qntd")
                enviar = driver.find_element(by=By.NAME, value="Add")
                categoria = driver.find_element(by=By.NAME, value="select")
                categoria = Select(categoria)

                categoria.select_by_visible_text("Cartas")
                foto.send_keys("https://i.imgur.com/aOQ23Z8.jpeg")
                prod.send_keys("Poker")
                descricao.send_keys("Cartas de Poker")
                preco.send_keys("2")
                qntd.send_keys("99")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

        self.assertTrue(
            True
        )
        driver.get("http://127.0.0.1:8000/logout/")

    def teste_001_cenario1(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("Teclado gamer")
        self.assertEquals(
            driver.find_element(by=By.NAME, value="vazio").text,
            "Nenhum produto disponível."
        )

    def teste_002_cenario2(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("pokémon")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))

    def teste_003_cenario3(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/")
        barra_de_categoria = driver.find_element(by=By.NAME, value="select")
        barra_de_categoria = Select(barra_de_categoria)
        barra_de_categoria.select_by_visible_text("Cartas")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))

    def teste_004_cenario4(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("Minis Recife")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))


