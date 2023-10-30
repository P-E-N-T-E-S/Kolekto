from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

segundos = 5

driver = webdriver.Chrome()

class Historia2(LiveServerTestCase):
    def test_000_setup(self):
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


class Historia3(LiveServerTestCase):
    def test_000_setup(self):
        for i in range(segundos):
            driver.get("http://127.0.0.1:8000/registro")
            usuario = driver.find_element(by=By.NAME, value="username")
            nome_usuario = driver.find_element(by=By.NAME, value="nome")
            email = driver.find_element(by=By.NAME, value="email")
            senha = driver.find_element(by=By.NAME, value="senha")
            botao = driver.find_element(by=By.NAME, value="registro")

            usuario.send_keys(f"Teste3{i}")
            nome_usuario.send_keys(f"Marcílio{i}")
            email.send_keys(f"hist3{i}@teste.com")
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
                time.sleep(2)
                enviar = driver.find_element(by=By.NAME, value="criar")

                nascimento.send_keys("29082003")
                cidade.send_keys("Rio Branco")
                cpf.send_keys("000.000.000-00")
                nome_loja.send_keys("Lojateste3")
                imgperfil.send_keys("https://i.imgur.com/FWUCFTF.jpeg")
                imgbanner.send_keys("https://i.imgur.com/T2umQUo.jpeg")
                descloja.send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
                time.sleep(2)
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

                foto.send_keys("https://i.ebayimg.com/images/g/HbYAAOSwKeVjOsBa/s-l1600.jpg")
                prod.send_keys('Black Lotus - Beta')
                descricao.send_keys("Black Lotus - Beta, uma das cartas mais raras do Magic")
                preco.send_keys("4039553")
                qntd.send_keys("1")
                categoria.select_by_visible_text("Cartas")
                time.sleep(segundos)
                enviar.send_keys(Keys.ENTER)
        self.assertTrue(
            True
        )
        driver.get("http://127.0.0.1:8000/logout/")

    def test_001_cenario1(self):
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste30")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)
        time.sleep(segundos)

        div = driver.find_element(by=By.NAME, value="Charizard 1999 - 1° Edição")
        idproduto = div.find_element(by=By.TAG_NAME, value="a").get_attribute("name")

        driver.get(f"http://127.0.0.1:8000/Produto/{idproduto}")
        time.sleep(segundos)

        favorito = driver.find_element(By.ID, value="adicionarListaDesejos")

        favorito.click()
        time.sleep(segundos)

        driver.get("http://127.0.0.1:8000/lista_desejos")

        self.assertEquals(
            driver.find_element(by=By.ID, value="Charizard 1999 - 1° Edição").text,
            "Charizard 1999 - 1° Edição"
        )
        driver.get("http://127.0.0.1:8000/logout")

    def test_002_cenario2(self):
        driver.get("http://127.0.0.1:8000")
        div = driver.find_element(by=By.NAME, value="Black Lotus - Beta")
        idproduto = div.find_element(by=By.TAG_NAME, value="a").get_attribute("name")
        driver.get(f"http://127.0.0.1:8000/Produto/{idproduto}")
        favorito = driver.find_element(By.ID, value="adicionarListaDesejos")

        favorito.click()
        time.sleep(segundos)
        self.assertEquals(
            driver.title,
            "Login"
        )

    def test_003_cenario3(self):
        driver.get("http://127.0.0.1:8000/login")

        usuario = driver.find_element(by=By.NAME, value="username")
        senha = driver.find_element(by=By.NAME, value="senha")
        enviar = driver.find_element(by=By.NAME, value="Logar")

        usuario.send_keys("Teste30")
        senha.send_keys("Teste12345")
        time.sleep(segundos)
        enviar.send_keys(Keys.ENTER)
        time.sleep(segundos)

        driver.get("http://127.0.0.1:8000/lista_desejos")

        idproduto = driver.find_element(by=By.ID, value="Charizard 1999 - 1° Edição").get_attribute("name")

        driver.get(f"http://127.0.0.1:8000/Produto/{idproduto}")

        favorito = driver.find_element(By.ID, value="adicionarListaDesejos")

        favorito.click()
        time.sleep(segundos)

        driver.get("http://127.0.0.1:8000/lista_desejos")

        try:
            driver.find_element(by=By.ID, value="Charizard 1999 - 1° Edição")
        except:
            validacao = True
        else:
            validacao = False

        self.assertTrue(
            validacao
        )


class Historia4(LiveServerTestCase):
    def test_000_setup(self):
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
        driver.get("http://127.0.0.1:8000/nova_loja")
        self.assertEquals(
            driver.title,
            "Login"
        )

    def teste_004_cenario4(self):
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




class Historia5(LiveServerTestCase):
    def test_000_setup(self):
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
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("Teclado gamer")
        self.assertEquals(
            driver.find_element(by=By.NAME,value="vazio").text,
            "Nenhum produto disponível."
        )

    def teste_002_cenario2(self):
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("pokémon")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))
    
    def teste_003_cenario3(self):
        driver.get("http://127.0.0.1:8000/")
        barra_de_categoria = driver.find_element(by=By.NAME, value="select")
        barra_de_categoria = Select(barra_de_categoria)
        barra_de_categoria.select_by_visible_text("Cartas")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))

    def teste_004_cenario4(self):
        driver.get("http://127.0.0.1:8000/")
        barra_de_pesquisa = driver.find_element(by=By.NAME, value="nome_pesquisado")
        barra_de_pesquisa.send_keys("Minis Recife")
        self.assertIsNotNone(driver.find_element(by=By.CLASS_NAME, value="card"))

class Historia7(LiveServerTestCase):
    def test_000_setup(self):
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


class Historia8(LiveServerTestCase):
    def test_000_setup(self):
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