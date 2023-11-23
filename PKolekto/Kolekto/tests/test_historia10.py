from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

segundos = 0

produto_nome = "Carta Pokemon: Charmander"
produto_preco = "10"


class Historia10(LiveServerTestCase):

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
            botao = driver.find_element(by=By.NAME, value="Logar")

            usuario.send_keys(f"Teste10{i}")
            nome_usuario.send_keys(f"Marcílio10{i}")
            email.send_keys(f"hist10{i}@teste.com")
            senha.send_keys("Teste12345")
            time.sleep(segundos)
            botao.send_keys(Keys.ENTER)

            if i == 0:
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
                nome_loja.send_keys("Lojateste10")
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
                prod.send_keys(produto_nome)
                descricao.send_keys("Charmander")
                preco.send_keys(produto_preco)
                qntd.send_keys("5")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

        else:
            time.sleep(0.5)
            idproduto = driver.find_element(by=By.NAME, value=f"{produto_nome} card").get_attribute("id")
            driver.get(f"http://127.0.0.1:8000/Produto/{idproduto}/")

            time.sleep(segundos)

            botao = driver.find_element(by=By.ID, value="adicionarCarrinho")
            botao.click()

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

        usuario.send_keys("Teste101")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/carrinho")
        tabela = driver.find_element(by=By.TAG_NAME, value="tr")
        nome = tabela.find_element(by=By.TAG_NAME, value="h5").text
        preco = tabela.find_element(by=By.ID, value="preco").text
        self.assertTrue(
            nome == produto_nome and preco == produto_preco
        )

    def test_002_cenario2(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste101")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

        driver.get("http://127.0.0.1:8000/carrinho")

        botao = driver.find_element(by=By.ID, value="Comprar")
        botao.click()

        self.assertEquals(
            driver.title,
            "Kolekto: Informações de pedido"
        )

    def test_003_cenario3(self):
        driver = setup_selenium()
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste101")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)

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
        cpf.send_keys("164.718.030-95")
        senha.send_keys("Teste12345")
        transporte.click()

        time.sleep(segundos)

        botao.send_keys(Keys.ENTER)

        tabela = driver.find_element(by=By.ID, value=produto_nome)
        nome = tabela.find_element(by=By.ID, value="nome").text
        preco = tabela.find_element(by=By.ID, value="preco").text

        self.assertTrue(
            nome == produto_nome and preco == produto_preco
        )
