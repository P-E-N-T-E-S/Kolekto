from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

segundos = 0

class Historia7(LiveServerTestCase):


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

            usuario.send_keys(f"Teste7{i}")
            nome_usuario.send_keys(f"Evaldo{i}")
            email.send_keys(f"hist7{i}@teste.com")
            senha.send_keys("Teste12345")
            botao.send_keys(Keys.ENTER)

            if i == 0:
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
                cidade.send_keys("Recife")
                cpf.send_keys("222.333.444-55")
                nome_loja.send_keys("Records")
                imgperfil.send_keys("https://i.imgur.com/7i6SwKD.jpeg")
                imgbanner.send_keys("https://i.imgur.com/AGdTdER.jpeg")
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
                foto.send_keys("https://i.etsystatic.com/29420651/r/il/3a4b26/3107994649/il_1080xN.3107994649_odus.jpg")
                prod.send_keys("Mega Mewtwo")
                descricao.send_keys("Mega Mewtwo, uma das cartas mais raras de Pokémon TCG")
                preco.send_keys("300")
                qntd.send_keys("30")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

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
                cidade.send_keys("Rio Doce")
                cpf.send_keys("111.333.124-23")
                nome_loja.send_keys("Moedas Antigas")
                imgperfil.send_keys("https://i.imgur.com/FWylmwo.jpeg")
                imgbanner.send_keys("https://i.imgur.com/cjrf7Wb.jpeg")
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
                foto.send_keys("https://cdn.awsli.com.br/600x450/208/208516/produto/39759641/0eab808129.jpg")
                prod.send_keys("Moeda Antiga")
                descricao.send_keys("Moeda antiga, 100 R$")
                preco.send_keys("100")
                qntd.send_keys("1")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

            if i == 2:
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
                nome_loja.send_keys("Arte em Miniatura")
                imgperfil.send_keys("https://i.imgur.com/YovkzzM.jpeg")
                imgbanner.send_keys("https://i.imgur.com/8FaMXR6.jpeg")
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

                categoria.select_by_visible_text("Arte")
                foto.send_keys("https://i.imgur.com/YovkzzM.jpeg")
                prod.send_keys("Miniatura de Pessoa dodoi")
                descricao.send_keys("Arte feita com uma pessoa dodoi")
                preco.send_keys("50")
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

                categoria.select_by_visible_text("Arte")
                driver.get("http://127.0.0.1:8000/add_produto")
                foto.send_keys("https://i.imgur.com/qbZkY4J.jpeg")
                prod.send_keys("Pessoas nadando")
                descricao.send_keys("Arte feita com uma pessoa nadando")
                preco.send_keys("150")
                qntd.send_keys("15")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)


        self.assertTrue(
            True
        )
        driver.get("http://127.0.0.1:8000/logout/")