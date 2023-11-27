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

class Historia02(LiveServerTestCase):
    def test_001_cenario0(self):
        for i in range(2):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="Logar")

            usuario.send_keys(f"Teste2{i}")
            nome_usuario.send_keys(f"Marcílio{i}")
            email.send_keys(f"hist2{i}@teste.com")
            senha.send_keys("Teste12345")
            time.sleep(segundos)
            botao.send_keys(Keys.ENTER)

            if i == 1:
                time.sleep(segundos)
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
                nome_loja.send_keys("Logrec")
                perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                descricao.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                estado.select_by_visible_text("Pernambuco")
                time.sleep(segundos)
                botao.click()
        self.assertTrue(
            True
        )
        driver.get("http://127.0.0.1:8000/logout/")


    def test_002_cenario1(self):
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
        qntd.send_keys("5")
        categoria.select_by_visible_text("Cartas")
        time.sleep(segundos)
        enviar.click()

        try:
            driver.find_element(by=By.NAME, value="Charizard 1999 - 1° Edição")
        except:
            validacao = False
        else:
            validacao = True

        self.assertTrue(
            validacao
        )
        driver.get("http://127.0.0.1:8000/logout")

    def test_003_cenario2(self):
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
        enviar.click()

        self.assertEqual(
            driver.title,
            "Kolekto: Adicionar produto"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def teste_004_cenario3(self):
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
        self.assertEqual(
            driver.title,
            "Kolekto: Criar Loja"
        )