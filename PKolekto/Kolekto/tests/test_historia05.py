from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


segundos = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)


class Historia05(LiveServerTestCase):
    def test_000_setup(self):
        for i in range(4):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="Logar")

            usuario.send_keys(f"Teste5{i}")
            nome_usuario.send_keys(f"Thomaz{i}")
            email.send_keys(f"hist5{i}@teste.com")
            senha.send_keys("Teste12345")
            botao.send_keys(Keys.ENTER)

            if i == 1:
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
                nome_loja.send_keys("Cartas Hype")
                perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                descricao.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                estado.select_by_visible_text("Pernambuco")
                time.sleep(segundos)
                botao.click()

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
                descricao.send_keys("Carta Pokémon do Charmander feita a mão")
                preco.send_keys("10")
                qntd.send_keys("5")
                time.sleep(segundos)
                enviar.click()

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
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("Teclado gamer")
        barra_de_pesquisa.send_keys(Keys.ENTER)
        self.assertEqual(
            driver.find_element(by=By.ID, value="vazio").text,
            "Nenhum produto disponível."
        )

    def teste_002_cenario2(self):
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("pokémon")
        barra_de_pesquisa.send_keys(Keys.ENTER)
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))

    def teste_003_cenario3(self):
        driver.get("http://127.0.0.1:8000/pesquisa?select=Cartas")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))

    def teste_004_cenario4(self):
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("Cartas Hype")
        barra_de_pesquisa.send_keys(Keys.ENTER)
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))


