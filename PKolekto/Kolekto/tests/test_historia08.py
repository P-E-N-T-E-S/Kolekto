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


class Historia08(LiveServerTestCase):

    def test_000_setup(self):
        for i in range(4):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="Logar")

            usuario.send_keys(f"Teste8{i}")
            nome_usuario.send_keys(f"Marcílio{i}")
            email.send_keys(f"hist8{i}@teste.com")
            senha.send_keys("Teste12345")
            time.sleep(segundos)
            botao.click()
            if i == 0:
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
                nome_loja.send_keys("Recicards")
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
                categoria = driver.find_element(by=By.NAME, value="select")
                categoria = Select(categoria)
                enviar = driver.find_element(by=By.NAME, value="Add")

                foto.send_keys("https://static22.minhalojanouol.com.br/brofistloja/produto/20210701161644_6137993863_D.jpg")
                prod.send_keys("Charizard 1999 - 1° Edição")
                descricao.send_keys("Carta Charizard 1999 - 1° Edição")
                preco.send_keys("99")
                qntd.send_keys("1")
                categoria.select_by_visible_text("Cartas")
                time.sleep(segundos)
                enviar.click()
                
            elif i == 2:
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
                nome_loja.send_keys("PokerMart")
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

                categoria.select_by_visible_text("Arte")
                foto.send_keys("https://i.ebayimg.com/images/g/HbYAAOSwKeVjOsBa/s-l1600.jpg")
                prod.send_keys("Pikachu Shiny - Edição Especial")
                descricao.send_keys("Pikachu Shiny - Edição Especial, uma das cartas mais raras do Magic")
                preco.send_keys("4039553")
                qntd.send_keys("2")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

            elif i == 3:
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
                nome_loja.send_keys("Art Gallery")
                perfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                descricao.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                estado.select_by_visible_text("Pernambuco")
                time.sleep(segundos)
                botao.click()

                time.sleep(segundos)
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
                foto.send_keys("https://d1o6h00a1h5k7q.cloudfront.net/imagens/img_m/9029/4041864.jpg")
                prod.send_keys("Mona Lisa Reprodução - Edição Limitada")
                descricao.send_keys("Mona Lisa Reprodução")
                preco.send_keys("1000")
                qntd.send_keys("3")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)
                
    def test_001_cenario1(self):
        driver.get("http://127.0.0.1:8000/login")
        
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste81")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)
        time.sleep(segundos)

        idproduto = driver.find_element(by=By.NAME, value="Charizard 1999 - 1° Edição card").get_attribute("id")
        
        driver.get(f"http://127.0.0.1:8000/Produto/{idproduto}")
        time.sleep(segundos)
        
        carrinho = driver.find_element(By.ID, value="adicionarCarrinho")
        carrinho.send_keys(Keys.ENTER)
        time.sleep(segundos)
        driver.get("http://127.0.0.1:8000/carrinho")

        validacao = driver.find_element(by=By.ID, value="Charizard 1999 - 1° Edição").text[:26] == "Charizard 1999 - 1° Edição"

        driver.get("http://127.0.0.1:8000/logout")

        self.assertTrue(validacao)
        
    def test_002_cenario2(self):
        driver.get("http://127.0.0.1:8000/logout")
        driver.get("http://127.0.0.1:8000")

        driver.get("http://127.0.0.1:8000/carrinho")

        time.sleep(segundos)
        self.assertEqual(
            driver.title,
            "Kolekto: Login"
        )
        
    def test_003_cenario3(self):
        driver.get("http://127.0.0.1:8000/login")
            
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste81")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)
        time.sleep(segundos)
        
        driver.get("http://127.0.0.1:8000/carrinho")
        
        remover = driver.find_element(by=By.ID, value="removerCarrinho")
        remover.send_keys(Keys.ENTER)
        time.sleep(segundos)

        driver.refresh()
        
        mensagem_carrinho_vazio = driver.find_element(by=By.TAG_NAME, value="h4")
        self.assertEqual(mensagem_carrinho_vazio.text, "Seu carrinho está vazio.")
        
        driver.get("http://127.0.0.1:8000/logout")
        
    def test_004_cenario4(self):
        driver.get("http://127.0.0.1:8000/login")
            
        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste81")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)
        time.sleep(segundos)

        idproduto = driver.find_element(by=By.NAME, value="Mona Lisa Reprodução - Edição Limitada card").get_attribute("id")

        driver.get(f"http://127.0.0.1:8000/Produto/{idproduto}")
        time.sleep(segundos)

        carrinho = driver.find_element(By.ID, value="adicionarCarrinho")
        carrinho.send_keys(Keys.ENTER)
        time.sleep(segundos)
        
        driver.get("http://127.0.0.1:8000/carrinho")
        
        add_qntd = driver.find_element(by=By.ID, value="addQntd")
        add_qntd.send_keys(Keys.ENTER)

        tabeladiv = driver.find_element(by=By.ID, value="Mona Lisa Reprodução - Edição Limitada")
        div = tabeladiv.find_element(by=By.ID, value="divisoria")
        texto = div.find_elements(by=By.TAG_NAME, value="h5")
        valorprod = texto[1].text
        valorprod = float(valorprod[2:].replace(',', '.'))

        valortot = driver.find_element(by=By.ID, value="total").text
        valortot = float(valortot[12:])
            
        self.assertTrue(
            valortot == 2*valorprod
        )
        
        
        