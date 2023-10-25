from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Produto, Loja, ListaDesejos
from django.http import Http404, JsonResponse
from django.db.models import Q
import json



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
        "temloja": temloja
    }
    
    if request.method == "POST":
        errado = False
        erros = {}

        data_nascimento = request.POST.get("nascimento")
        Localizacao = f"{request.POST.get('cidade')}, {request.POST.get('estado')}"
        cpf = request.POST.get("cpf")
        nome_loja = request.POST.get("nome_loja")
        banner = request.POST.get("banner")
        perfil = request.POST.get("perfil")
        associado = usuario
        descricao = request.POST.get("descricao")
        
        if Loja.objects.filter(NomeLoja=nome_loja).exists():
            erros["nomedaloja"] = "Já existe uma loja com esse nome."
            errado = True

        if banner[-5:-1] != ".jpe" or perfil[-5:-1] != ".jpe":
            erros["urlerrado"] = "O url da imagem está com erro, por favor clique com o botão direito e copie o endereço da imagem"
            errado = True

        if errado:
            contexto["erros"] = erros
            contexto["data_nascimento"] = data_nascimento
            contexto["localizacao"] = request.POST.get("cidade")
            contexto["estado"] = True
            contexto["cpf"] = cpf
            contexto["nome_loja"] = nome_loja
            contexto["banner"] = banner
            contexto["perfil"] = perfil
            contexto["descrito"] = descricao
            return render(request, "cadastro_loja.html", context=contexto)
        else:
            try:
                Loja.objects.create(Banner=banner, Perfil=perfil, NomeLoja=nome_loja, associado=associado, Cpf=cpf,
                            DataNascimento=data_nascimento, Localizacao=Localizacao, descricao=descricao)
            except:
                contexto["erros"] = "Preencha todos os campos corretamente."
                contexto["data_nascimento"] = data_nascimento
                contexto["localizacao"] = request.POST.get("cidade")
                contexto["estado"] = True
                contexto["cpf"] = cpf
                contexto["nome_loja"] = nome_loja
                contexto["banner"] = banner
                contexto["perfil"] = perfil
                contexto["descrito"] = descricao
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
    else:
        lista_existente = ListaDesejos.objects.filter(usuario=usuario, produto=id_produto.id).exists()
        if Loja.objects.filter(associado_id=usuario).exists():
            temloja = True
        else:
            temloja = False
    
    loja = id_produto.loja
    nome_loja = loja.NomeLoja
    if id_produto is not None:
        contexto = {
            "lista_existente":lista_existente,
            "id_produto": id_produto.id,
            "foto1": id_produto.foto1,
            "nome_produto": id_produto.nome_produto,
            "descricao": id_produto.descricao,
            "preco": id_produto.preco,
            "categoria": id_produto.categoria,
            "qntd": id_produto.qntd,
            "nome_loja": nome_loja,
            "temloja": temloja
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
    contexto = {
        "temloja": temloja
    }
    if loja is not None:
        produtos = list(loja.produto_set.all())
        contexto = {
            "banner": loja.Banner,
            "perfil": loja.Perfil,
            "nome_loja": loja.NomeLoja,
            "localizacao": loja.Localizacao,
            "descricao": loja.descricao,
            "produtos": produtos,
            "temloja": temloja
        }
        return render(request, "pagina_loja.html", context=contexto)
    else:
        raise Http404("Loja não encontrada")


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
            "banner": loja.Banner,
            "perfil": loja.Perfil,
            "nome_loja": loja.NomeLoja,
            "localizacao": loja.Localizacao,
            "descricao": loja.descricao,
            "produtos": produtos,
            "temloja": temloja
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