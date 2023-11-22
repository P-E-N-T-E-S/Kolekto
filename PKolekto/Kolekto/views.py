from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Produto, Loja, ListaDesejos, Carrinho, Compra, Avaliacao
from django.http import Http404, JsonResponse
from django.db.models import Q
from django.core.mail import send_mail
import json
from .utils import *



categorias = [
                "Selecione a categoria",
                "Móveis e Decoração",
                "Arte",
                "Joalheria",
                "Livros",
                "Relógios",
                "Cartas",
                "Brinquedos e Jogos",
                "Vestuário",
                "Fotografia",
                "Instrumento Musical",
                "Outro"
            ]

estados_brasileiros = [
    "Acre",
    "Alagoas",
    "Amapá",
    "Amazonas",
    "Bahia",
    "Ceará",
    "Distrito Federal",
    "Espírito Santo",
    "Goiás",
    "Maranhão",
    "Mato Grosso",
    "Mato Grosso do Sul",
    "Minas Gerais",
    "Pará",
    "Paraíba",
    "Paraná",
    "Pernambuco",
    "Piauí",
    "Rio de Janeiro",
    "Rio Grande do Norte",
    "Rio Grande do Sul",
    "Rondônia",
    "Roraima",
    "Santa Catarina",
    "São Paulo",
    "Sergipe",
    "Tocantins"
]

def Registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {"erro": "Usuário já existe"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'registro.html', {"erro": "Email já está sendo usado"})

        user = User.objects.create_user(username=username, password=senha, email=email, first_name=nome)
        login(request, user)
        request.session["usuario"] = username
        return redirect(home)
        
    return render(request, 'registro.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            request.session["usuario"] = username
            return redirect(home)
        else:
            return render(request, 'login.html', {"erro": "Usuário não encontrado"})
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    
    if "usuario" in request.session:
        del request.session["usuario"]
    return redirect(home)


@login_required
def Cadastro_Loja(request):
    usuario = request.user

    if Loja.objects.filter(associado_id=usuario).exists():
        temloja = True
    else:
        temloja = False
        
    contexto = {
        "nome_vendedor": usuario.first_name,
        "temloja": temloja,
        "estados_brasileiros": estados_brasileiros
    }
    
    if request.method == "POST":
        errado = False
        erros = {}
        cidade = request.POST.get("Rua/Avenida")
        estado = request.POST.get("estado")
        data_nascimento = request.POST.get("nascimento")
        Localizacao = f"{cidade}, {estado}"
        cpf = request.POST.get("cpf")
        nome_loja = request.POST.get("nome_loja")
        perfil = request.POST.get("perfil")
        associado = usuario
        descricao = request.POST.get("descricao")

        if nomeLojaExiste(nome_loja):
            errado = True
            erros["nomedaloja"] = "Já existe uma loja com esse nome."

        if validacaoLinks(perfil):
            errado = True
            erros["urlerrado"] = "O url da imagem está com erro, por favor clique com o botão direito e copie o endereço da imagem"

        if validar_cpf(cpf):
            errado = True
            erros["cpferrado"] = "digite o cpf corretamente"

        if request.POST.get("estado") == None:
            errado = True
            erros["selecestado"] = "selecione o seu estado"

        if errado:
            contexto["erros"] = erros
            contexto["data_nascimento"] = data_nascimento
            contexto["localizacao"] = request.POST.get("cidade")
            contexto["estado"] = True
            contexto["selecao"] = {request.POST.get('estado')}
            contexto["cpf"] = cpf
            contexto["nome_loja"] = nome_loja
            contexto["perfil"] = perfil
            contexto["descrito"] = descricao
            contexto["estado_resposta"] = estado
            contexto["estados_brasileiros"] = estados_brasileiros
            return render(request, "cadastro_loja.html", context=contexto)
        else:
            try:
                Loja.objects.create(Perfil=perfil, NomeLoja=nome_loja, associado=associado, Cpf=cpf,
                            DataNascimento=data_nascimento, Localizacao=Localizacao, descricao=descricao)
            except:
                contexto["erros"] = "Preencha todos os campos corretamente."
                contexto["data_nascimento"] = data_nascimento
                contexto["localizacao"] = request.POST.get("cidade")
                contexto["estado"] = True
                contexto["selecao"] = {request.POST.get('estado')}
                contexto["cpf"] = cpf
                contexto["nome_loja"] = nome_loja
                contexto["perfil"] = perfil
                contexto["descrito"] = descricao
                contexto["estado_resposta"] = estado
                contexto["estados_brasileiros"] = estados_brasileiros
                return render(request, "cadastro_loja.html", context=contexto)
            else:
                return redirect(home)
    return render(request, "cadastro_loja.html", context=contexto)


@login_required
def Add_Produto(request):
    erros = {}
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False 
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    loja = usuario.loja_set.all()
    if len(list(loja)) == 0:
        return redirect(Cadastro_Loja)
    else:
        categorias = [
            "Selecione a categoria",
            "Móveis e Decoração",
            "Arte",
            "Joalheria",
            "Livros",
            "Relógios",
            "Cartas",
            "Brinquedos e Jogos",
            "Vestuário",
            "Fotografia",
            "Instrumento Musical",
            "Outro"
        ]

        if request.method == "POST":
            errado = False
            foto1 = request.POST.get("foto1")
            nome_produto = request.POST["nome_produto"]
            descricao = request.POST["descricao"]
            preco = request.POST["preco"]
            categoria = request.POST["select"]
            qntd = request.POST["qntd"]

            if not nome_produto or not descricao or not preco or not qntd or foto1 is None or categoria == "Selecione a categoria":
                erros["campos"] = "Preencha todos os campos necessários"
                errado = True
            if foto1[-5:-1] != ".jpe":
               erros["url"] = "O url da imagem está com erro, por favor clique com o botão direito e copie o endereço da imagem"

            if errado:
                contexto = {
                    "erros": erros,
                    "foto1": foto1,
                    "nome_produto": nome_produto,
                    "descricao": descricao,
                    "preco": preco,
                    "qntd": qntd,
                    "categorias": categorias,
                    "temloja": temloja
                }
                return render(request, "add_produto.html", contexto)
                
            try:
                Produto.objects.create(foto1=foto1, nome_produto=nome_produto, descricao=descricao, preco=preco, categoria=categoria, qntd=qntd, loja=loja[0])
            except:
                erros["precos"] = "Insira um valor válido"
                contexto = {
                    "erros": erros,
                    "foto1": foto1,
                    "nome_produto": nome_produto,
                    "descricao": descricao,
                    "preco": preco,
                    "qntd": qntd,
                    "erropreco": "Coloque um preço válido",
                    "categorias": categorias,
                    "temloja": temloja
                }
                return render(request, "add_produto.html", contexto)
            else:
                loja[0].NomeLoja
                return redirect(home)
        return render(request, "add_produto.html", {"categorias": categorias, "temloja": temloja})

       
def pagina_produto(request, id_produto):
    usuario = request.user
    id_produto = Produto.objects.get(id=id_produto)
    if request.user.is_anonymous:
        temloja = False 
        lista_existente = None
        carrinho_existente = None
    else:
        lista_existente = ListaDesejos.objects.filter(usuario=usuario, produto=id_produto.id).exists()
        carrinho_existente = Carrinho.objects.filter(usuario=usuario, produto=id_produto.id).exists()
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False
    
    loja = id_produto.loja
    nome_loja = loja.NomeLoja
    foto_loja = loja.Perfil
    if id_produto is not None:
        contexto = {
            "lista_existente":lista_existente,
            "carrinho_existente": carrinho_existente,
            "id_produto": id_produto.id,
            "foto1": id_produto.foto1,
            "nome_produto": id_produto.nome_produto,
            "descricao": id_produto.descricao,
            "preco": id_produto.preco,
            "categoria": id_produto.categoria,
            "qntd": id_produto.qntd,
            "nome_loja": nome_loja,
            "temloja": temloja,
            "foto_loja": foto_loja,
        }

        return render(request, "pagina_produto.html", context=contexto)
    else:
        raise Http404("Produto não encontrado")


def home(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False 
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False
    
    produtos = Produto.objects.all()
    contexto = {
        "categorias":categorias,
        "temloja": temloja,
        "produtos": produtos
    }
    return render(request, "home.html", context=contexto)


def pesquisa(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False 
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    nome_pesquisado = request.GET.get("nome_pesquisado")
    if nome_pesquisado is None:
        nome_pesquisado = ""
    categoria = request.GET.get("select")

    if categoria is None:
        categoria = "" 
        
    if nome_pesquisado:
        if categoria:
            lista_produtos = Produto.objects.filter(Q(nome_produto__icontains=nome_pesquisado)
            | Q(descricao__icontains=nome_pesquisado)
            | Q(categoria__icontains=categoria)
            | Q(loja__NomeLoja__icontains=nome_pesquisado))
        else:
            lista_produtos = Produto.objects.filter(Q(nome_produto__icontains=nome_pesquisado)
            | Q(descricao__icontains=nome_pesquisado)
            | Q(loja__NomeLoja__icontains=nome_pesquisado))
    else:
        if categoria != "Selecione a categoria":
            lista_produtos = Produto.objects.filter(Q(categoria__icontains=categoria))
        else:
            return render(request, 'home.html', {"erro": "Por Favor Digite um produto","categorias":categorias})

    contexto = {
        "nome_pesquisado":nome_pesquisado,
        "categoria":categoria,
        "lista_produtos":lista_produtos,
        "temloja": temloja
    }
    return render(request, "pesquisa.html", context=contexto)


def pagina_loja(request, nome_loja):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    loja = Loja.objects.get(NomeLoja=nome_loja)
    if loja is not None:
        produtos = list(loja.produto_set.all())
        contexto = {
            "minhaloja": False,
            "perfil": loja.Perfil,
            "nome_loja": loja.NomeLoja,
            "localizacao": loja.Localizacao,
            "descricao": loja.descricao,
            "produtos": produtos,
            "temloja": temloja,
            "avaliacoes": list(loja.avaliacao_set.all())
        }
        return render(request, "pagina_loja.html", context=contexto)
    else:
        raise Http404("Loja não encontrada")


@login_required
def denuncia(request, nome_loja):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False 
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    motivo = request.POST.get("motivo")
    detalhes = request.POST.get("detalhes")
    
    if request.method == 'POST':
        try:
            send_mail(
                    (f"Nova Denúncia: {nome_loja}"),
                    (f"Loja denunciada: {nome_loja}\nMotivo da denúncia: {motivo}\nDescrição da denúncia: {detalhes} \nRealizada por: {usuario}"),
                    "pkolekto@gmail.com",
                    ["suporte.kolekto@gmail.com"],
                    fail_silently=False,
                )
        finally:
            return redirect(home)

    contexto = {
        "motivo": motivo,
        "detalhes": detalhes,
        "usuario": usuario,
        "temloja": temloja
    }

    return render(request, "denuncia.html", context=contexto)


@login_required
def minha_loja(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False 
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    loja = Loja.objects.get(associado_id=usuario.id)
    if loja is not None:
        produtos = list(loja.produto_set.all())
        contexto = {
            "minhaloja": True,
            "perfil": loja.Perfil,
            "nome_loja": loja.NomeLoja,
            "localizacao": loja.Localizacao,
            "descricao": loja.descricao,
            "produtos": produtos,
            "temloja": temloja,
            "avaliacoes": list(loja.avaliacao_set.all())
        }
        return render(request, "pagina_loja.html", context=contexto)
    else:
        raise Http404("Loja não encontrada")
    

@login_required
def lista_desejos(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False 
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    lista = ListaDesejos.objects.filter(usuario=usuario.id)
        
    if lista is not None:
        produtos = []
        for nome in lista:
            produtos.append(Produto.objects.get(id=nome.produto.id))
        return render(request, "lista_desejos.html", {"produtos": produtos, "temloja": temloja})
    
    return render(request, "lista_desejos.html", {"lista": lista})


@login_required
def add_lista_desejos(request):
    produto_id = json.loads(request.body)["produtoId"]
    id_produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        usuario = request.user
        
        lista_existente = ListaDesejos.objects.filter(usuario=usuario, produto=produto_id).exists()
        
        if not lista_existente:
            ListaDesejos.objects.create(usuario=usuario, produto=id_produto)
            return JsonResponse({'mensagem': "Produto adicionado à lista de desejos!"})
        else:
            return JsonResponse({'mensagem': 'Produto já adicionado.'}, status =302)
        
    return JsonResponse({'mensagem': 'Requisição inválida.'}, status=400)
    

@login_required
def rem_lista_desejos(request):
    produto_id = json.loads(request.body)["produtoId"]
    print(produto_id)
    if request.method == 'POST':
        usuario = request.user
        
        ListaDesejos.objects.filter(usuario=usuario, produto=produto_id).delete()
        return JsonResponse({'mensagem': 'Produto removido.'}, status=200)
           
    return JsonResponse({'mensagem': 'Requisição inválida.'}, status=400)


@login_required
def add_carrinho(request):
    produto_id = json.loads(request.body)["produtoId"]
    id_produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        usuario = request.user

        carrinho_existente = Carrinho.objects.filter(usuario=usuario, produto=produto_id).exists()

        if carrinho_existente:
            return JsonResponse({'mensagem': 'Produto já adicionado.'}, status=302)
        else:
            Carrinho.objects.create(usuario=usuario, produto=id_produto, quantidade=1)
            return JsonResponse({'mensagem': "Produto adicionado ao carrinho!"})

    return JsonResponse({'mensagem': 'Requisição inválida.'}, status=400)


@login_required
def rem_carrinho(request):
    produto_id = json.loads(request.body)["produtoId"]
    if request.method == 'POST':
        usuario = request.user

        Carrinho.objects.filter(usuario=usuario, produto=produto_id).delete()
        return JsonResponse({'mensagem': 'Produto removido.'}, status=200)

    return JsonResponse({'mensagem': 'Requisição inválida.'}, status=400)


@login_required
def carrinho(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    lista = Carrinho.objects.filter(usuario=usuario.id)

    if lista is not None:
        produtos = []
        soma = 0
        for nome in lista:
            produto = Produto.objects.get(id=nome.produto.id)
            produtos.append(produto)
            soma += produto.qntd * produto.preco
        return render(request, "carrinho.html", {"produtos": produtos, "temloja": temloja, "soma": soma})

    return render(request, "carrinho.html", {"lista": lista})

@login_required
def editar_loja(request, loja):
    usuario = request.user

    userloja = Loja.objects.get(NomeLoja=loja)
    if userloja.associado.username != usuario.username:
        return redirect(home)
    else:
        localizacao = (userloja.Localizacao).split(",")
        contexto = {
            "nome_vendedor": usuario.first_name,
            "temloja": True,
            "data_nascimento": userloja.DataNascimento,
            "cidade": localizacao[0],
            "estado": localizacao[1],
            "cpf": userloja.Cpf,
            "nome_loja": userloja.NomeLoja,
            "perfil": userloja.Perfil,
            "descrito": userloja.descricao,
            "estados_brasileiros": estados_brasileiros
        }

        if request.method == "POST":
            errado = False
            erros = {}

            data_nascimento = request.POST.get("nascimento")
            Localizacao = f"{request.POST.get('cidade')}, {request.POST.get('estado')}"
            cpf = request.POST.get("cpf")
            nome_loja = request.POST.get("nome_loja")
            perfil = request.POST.get("perfil")
            descricao = request.POST.get("descricao")

            if nomeLojaExiste(nome_loja):
                errado = True
                erros["nomedaloja"] = "Já existe uma loja com esse nome."

            if validacaoLinks(perfil):
                errado = True
                erros[
                    "urlerrado"] = "O url da imagem está com erro, por favor clique com o botão direito e copie o endereço da imagem"

            if validar_cpf(cpf):
                errado = True
                erros["cpferrado"] = "digite o cpf corretamente"

            if errado:
                contexto["erros"] = erros
                contexto["data_nascimento"] = data_nascimento
                contexto["localizacao"] = request.POST.get("cidade")
                contexto["estado"] = localizacao[1]
                contexto["cpf"] = cpf
                contexto["nome_loja"] = nome_loja
                contexto["perfil"] = perfil
                contexto["descrito"] = descricao
                return render(request, "editLoja.html", context=contexto)
            else:
                try:
                    userloja.NomeLoja = nome_loja
                    userloja.Perfil = perfil
                    userloja.Cpf = cpf
                    userloja.DataNascimento = data_nascimento
                    userloja.Localizacao = Localizacao
                    userloja.descricao = descricao
                    userloja.save()
                except:
                    contexto["erros"] = "Preencha todos os campos corretamente."
                    contexto["data_nascimento"] = data_nascimento
                    contexto["estado"] = True
                    contexto["cpf"] = cpf
                    contexto["nome_loja"] = nome_loja
                    contexto["perfil"] = perfil
                    contexto["descrito"] = descricao
                    contexto["estados_brasileiros"] = estados_brasileiros
                    return render(request, "editLoja.html", context=contexto)
                else:
                    return redirect(minha_loja)
        return render(request, "editLoja.html", context=contexto)


def realizar_compra(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False
    usuario = request.user
    compras = list(usuario.carrinho_set.all())
    produtos = list()
    soma = 0
    for nome in compras:
        produto = Produto.objects.get(id=nome.produto.id)
        produtos.append(produto)
        soma += nome.quantidade * produto.preco
    oplojas = list()
    for item in produtos:
        loja = item.loja
        oplojas.append(loja.NomeLoja)
    lojas = list(set(oplojas))
    sepcompras = list(range(len(lojas)))
    for i in range(len(lojas)):
        sepcompras[i] = dict()
        sepcompras[i]["loja"] = lojas[i]
        sepcompras[i]["produtos"] = [produto for produto in produtos if produto.loja.NomeLoja == lojas[i]]

    if request.method == "POST":
        cpf = request.POST.get("CPF")
        nome_comprador = request.POST.get("nome")
        cidade = request.POST.get("cidade")
        endereco = request.POST.get("endereço")
        complemento = request.POST.get("Complemento")
        transportadora = request.POST.get("Transportadora")
        senha = request.POST.get("confirmPassword")

        destino = f"{endereco}, {complemento}, {cidade}"
        erros = dict()

        errado = False

        if validar_cpf(cpf):
            errado = True
            erros["cpferrado"] = "Digite o CPF corretamente"

        if valida_senha(senha, request):
            errado = True
            erros["senhaerrada"] = "Insira sua senha corretamente"


        if errado:
            contexto = {
                "temloja":temloja,
                "erros": erros,
                "nome": nome_comprador,
                "compras": sepcompras,
                "valormax": soma,
                "cpf": cpf,
                "cidade": cidade,
                "endereco": endereco,
                "complemento": complemento,
            }
            return render(request, "realcompra.html", context=contexto)
        else:
            try:
                for nomeloja in lojas:
                    loja = Loja.objects.get(NomeLoja=nomeloja)
                    for opcao in sepcompras:
                        if opcao["loja"] == loja.NomeLoja:
                            compra = ''
                            for itens in opcao["produtos"]:
                                quantidade = list(usuario.carrinho_set.filter(produto=itens))
                                if len(quantidade) > 0:
                                    compra += f"{itens.pk};{quantidade[0].quantidade}/"
                                    quantidade[0].delete()
                    Compra.objects.create(usuario=usuario, loja=loja, transportadora=transportadora,
                                        destinatario=destino, valor=soma, itens=compra, nome_comprador=nome_comprador)
            except:
                erros["invalido"] = "Preencha os valores corretamente"
                contexto = {
                        "temloja": temloja,
                        "erros": erros,
                        "nome": nome_comprador,
                        "compras": sepcompras,
                        "valormax": soma,
                        "cpf": cpf,
                        "cidade": cidade,
                        "endereco": endereco,
                        "complemento": complemento,
                        "transportadora": transportadora
                    }
                return render(request, "realcompra.html", context=contexto)
            else:
                return redirect(historico_compras)
    contexto = {
        "temloja": temloja,
        "compras": sepcompras,
        "valormax": soma
    }
    return render(request, "realcompra.html", context=contexto)


def historico_compras(request):
    usuario = request.user
    if request.user.is_anonymous:
        temloja = False
    else:
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False

    compras = list(usuario.compra_set.all())
    separador = list()
    for compra in compras:
        produtos = list()
        chaves = [chave.split(";")[0] for chave in compra.itens.split("/") if chave.split(";")[0] != '']
        quantidades = [chave.split(";")[1] for chave in compra.itens.split("/") if chave.split(";")[0] != '']
        for chave in range(len(chaves)):
            produtos.append({
                "produto": Produto.objects.get(pk=chaves[chave]),
                "quantidade": quantidades[chave]
            })
        separador.append({
            "loja": f"{compra.loja} - {compra.data}",
            "produtos": produtos
        })
    contexto = {
        "temloja": temloja,
        "compras": separador,
        "infocompras": compras
    }
    return render(request, "historico.html", contexto)


@login_required
def avaliacao(request, id):
    usuario = request.user
    produto = Produto.objects.get(id=id)
    contexto={
        "loja": produto.loja
    }
    if Avaliacao.objects.filter(avaliador=usuario, loja=produto.loja).exists():
        return JsonResponse({'mensagem': 'Produto já avaliado.'}, status=200)
    else:
        if request.method == "POST":
            nota = request.POST.get("nota")
            comentario = request.POST.get("comentario")
            Avaliacao.objects.create(avaliador=usuario, loja=produto.loja, nota=nota, comentario=comentario)
            return redirect(historico_compras)

        return render(request, "avaliacao.html", contexto)