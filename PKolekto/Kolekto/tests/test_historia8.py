from selenium_setup import setup_selenium, finalizar_selenium
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

segundos = 0


class Historia8(LiveServerTestCase):

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

            usuario.send_keys(f"Teste8{i}")
            nome_usuario.send_keys(f"Marcílio{i}")
            email.send_keys(f"hist8{i}@teste.com")
            senha.send_keys("Teste12345")
            time.sleep(segundos)
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

                nascimento.send_keys("24112004")
                cidade.send_keys("Goiana")
                cpf.send_keys("999.999.999-99")
                nome_loja.send_keys("Recicards")
                imgperfil.send_keys("https://i.imgur.com/KxTGknf.jpeg")
                imgbanner.send_keys("https://i.imgur.com/AGdTdER.jpeg")
                descloja.send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

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
                enviar.send_keys(Keys.ENTER)

            elif i == 1:
                driver.get("http://127.0.0.1:8000/nova_loja")
                nascimento = driver.find_element(by=By.NAME, value="nascimento")
                cidade = driver.find_element(by=By.NAME, value="cidade")
                cpf = driver.find_element(by=By.NAME, value="cpf")
                nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
                imgperfil = driver.find_element(by=By.NAME, value="perfil")
                imgbanner = driver.find_element(by=By.NAME, value="banner")
                descloja = driver.find_element(by=By.NAME, value="descricao")
                enviar = driver.find_element(by=By.NAME, value="criar")

                nascimento.send_keys("24112004")
                cidade.send_keys("Recife")
                cpf.send_keys("222.222.222-22")
                nome_loja.send_keys("Magicrecife")
                imgperfil.send_keys("https://i.imgur.com/JtUNCXo.jpeg")
                imgbanner.send_keys("https://i.imgur.com/RhCYjb3.jpeg")
                descloja.send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

                driver.get("http://127.0.0.1:8000/add_produto")
                foto = driver.find_element(by=By.NAME, value="foto1")
                prod = driver.find_element(by=By.NAME, value="nome_produto")
                descricao = driver.find_element(by=By.NAME, value="descricao")
                preco = driver.find_element(by=By.NAME, value="preco")
                qntd = driver.find_element(by=By.NAME, value="qntd")
                enviar = driver.find_element(by=By.NAME, value="Add")
                categoria = Select(categoria)

                categoria.select_by_visible_text("Carta")
                foto.send_keys("https://i.ebayimg.com/images/g/HbYAAOSwKeVjOsBa/s-l1600.jpg")
                prod.send_keys("Black Lotus - Beta")
                descricao.send_keys("Black Lotus - Beta, uma das cartas mais raras do Magic")
                preco.send_keys("4039553")
                qntd.send_keys("1")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

            elif i == 2:
                driver.get("http://127.0.0.1:8000/nova_loja")
                nascimento = driver.find_element(by=By.NAME, value="nascimento")
                cidade = driver.find_element(by=By.NAME, value="cidade")
                cpf = driver.find_element(by=By.NAME, value="cpf")
                nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
                imgperfil = driver.find_element(by=By.NAME, value="perfil")
                imgbanner = driver.find_element(by=By.NAME, value="banner")
                descloja = driver.find_element(by=By.NAME, value="descricao")
                enviar = driver.find_element(by=By.NAME, value="criar")

                nascimento.send_keys("24112004")
                cidade.send_keys("Recife")
                cpf.send_keys("444.444.444-44")
                nome_loja.send_keys("PokeMart")
                imgperfil.send_keys("https://i.imgur.com/06jmo4M.png")
                imgbanner.send_keys("https://i.pinimg.com/1200x/2b/1d/fe/2b1dfec19b945a19ac39641278a6a799.jpg")
                descloja.send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)

                driver.get("http://127.0.0.1:8000/add_produto")
                foto = driver.find_element(by=By.NAME, value="foto1")
                prod = driver.find_element(by=By.NAME, value="nome_produto")
                descricao = driver.find_element(by=By.NAME, value="descricao")
                preco = driver.find_element(by=By.NAME, value="preco")
                qntd = driver.find_element(by=By.NAME, value="qntd")
                enviar = driver.find_element(by=By.NAME, value="Add")
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
                nascimento = driver.find_element(by=By.NAME, value="nascimento")
                cidade = driver.find_element(by=By.NAME, value="cidade")
                cpf = driver.find_element(by=By.NAME, value="cpf")
                nome_loja = driver.find_element(by=By.NAME, value="nome_loja")
                imgperfil = driver.find_element(by=By.NAME, value="perfil")
                imgbanner = driver.find_element(by=By.NAME, value="banner")
                descloja = driver.find_element(by=By.NAME, value="descricao")
                enviar = driver.find_element(by=By.NAME, value="criar")

                nascimento.send_keys("24112004")
                cidade.send_keys("Recife")
                cpf.send_keys("111.444.111-44")
                nome_loja.send_keys("ArtGallery")
                imgperfil.send_keys("https://upload.wikimedia.org/wikipedia/commons/1/18/OlindaGraffiti.jpg")
                imgbanner.send_keys("https://cdn.culturagenial.com/imagens/afinal-o-que-e-arte-og.jpg")
                descloja.send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum")
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
                categoria = Select(categoria)

                categoria.select_by_visible_text("Arte")
                foto.send_keys("https://d1o6h00a1h5k7q.cloudfront.net/imagens/img_m/9029/4041864.jpg")
                prod.send_keys("Mona Lisa Reprodução - Edição Limitada")
                descricao.send_keys("Mona Lisa Reprodução - Edição Limitada, uma das cartas mais raras do Magic")
                preco.send_keys("1000")
                qntd.send_keys("3")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)