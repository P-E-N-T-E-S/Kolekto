from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

segundos = 5

lojas = ['MagicTreasures', 'TechWonders', 'FashionEmporium']
produtos = ['X', 'Y', 'Z']

class Historia09(LiveServerTestCase):

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
            botao = driver.find_element(by=By.NAME, value="Logar")

            usuario.send_keys(f"Teste9{i}")
            nome_usuario.send_keys(f"Marcílio9{i}")
            email.send_keys(f"hist9{i}@teste.com")
            senha.send_keys("Teste12345")
            time.sleep(segundos)
            botao.send_keys(Keys.ENTER)

            if i < 4:
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
                nome_loja.send_keys(lojas[i])
                imgperfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                imgbanner.send_keys("https://i.imgur.com/T2umQUo.jpeg")
                descloja.send_keys(
                    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
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
                prod.send_keys(produtos[i])
                descricao.send_keys("Charmander")
                preco.send_keys('2')
                qntd.send_keys("5")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

        else:
            for j in range(3):
                time.sleep(0.5)
                produto = driver.find_element(by=By.NAME, value=produtos[j])
                produto.click()

                time.sleep(segundos)

                botao = driver.find_element(by=By.ID, value="adicionarCarrinho")
                botao.click()

            driver.get("http://127.0.0.1:8000/carrinho")

            botao = driver.find_element(by=By.ID, value="Comprar")
            botao.click()

            nome_entrega = driver.find_element(by=By.ID, value="nome")
            cidade = driver.find_element(by=By.ID, value="cidade")
            rua = driver.find_element(by=By.ID, value="Rua/Avenida")
            complemento = driver.find_element(by=By.ID, value="Complemento")
            cpf = driver.find_element(by=By.ID, value="CPF")
            senha = driver.find_element(by=By.ID, value="confirmPassword")
            transporte = driver.find_element(by=By.ID, value="Sedex")
            botao = driver.find_element(by=By.ID, value="Continuar")

            nome_entrega.send_keys("marcilio")
            cidade.send_keys("cidade dos bobos - BO")
            rua.send_keys("rua dos bobos")
            complemento.send_keys("0")
            cpf.send_keys("966.653.020-16")
            senha.send_keys("Teste12345")
            transporte.click()

            time.sleep(segundos)

            botao.send_keys(Keys.ENTER)

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

        usuario.send_keys("Teste94")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/historico_compra")

        botao = driver.find_element(by=By.ID, value="avaliar X")
        botao.click()

        comentario = driver.find_element(by=By.ID, value="comentario")
        nota = driver.find_element(by=By.ID, value="nota")
        botao = driver.find_element(by=By.ID, value="enviar")
        comentario.send_keys("produto veio com atraso")
        nota.send_keys("3")
        botao.click()

        driver.get("http://127.0.0.1:8000/MagicTreasures/")
        comentario = driver.find_element(by=By.ID, value="comentario Teste94")
        nota = driver.find_element(by=By.ID, value="nota Teste94")
        self.assertTrue(
            comentario.text == "produto veio com atraso" and nota.text == "3"
        )

    def test_002_cenario2(self):
        driver = setup_selenium()

        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste94")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/historico_compra")

        botao = driver.find_element(by=By.ID, value="avaliar Y")
        botao.click()

        comentario = driver.find_element(by=By.ID, value="comentario")
        nota = driver.find_element(by=By.ID, value="nota")
        botao = driver.find_element(by=By.ID, value="enviar")
        comentario.send_keys("produto veio com defeitos")
        nota.send_keys("1")
        botao.click()

        driver.get("http://127.0.0.1:8000/TechWonders/")
        comentario = driver.find_element(by=By.ID, value="comentario Teste94")
        nota = driver.find_element(by=By.ID, value="nota Teste94")
        self.assertTrue(
            comentario.text == "produto veio com defeitos" and nota.text == "1"
        )

    def test_003_cenario3(self):
        driver = setup_selenium()

        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste94")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/historico_compra")

        botao = driver.find_element(by=By.ID, value="avaliar X")
        botao.click()

        comentario = driver.find_element(by=By.ID, value="comentario")
        nota = driver.find_element(by=By.ID, value="nota")
        botao = driver.find_element(by=By.ID, value="enviar")
        comentario.send_keys("produto veio no tempo certo e com tudo ok")
        nota.send_keys("5")
        botao.click()

        driver.get("http://127.0.0.1:8000/MagicTreasures/")
        comentario = driver.find_element(by=By.ID, value="comentario Teste94")
        nota = driver.find_element(by=By.ID, value="nota Teste94")
        self.assertTrue(
            comentario.text == "produto veio no tempo certo e com tudo ok" and nota.text == "5"
        )