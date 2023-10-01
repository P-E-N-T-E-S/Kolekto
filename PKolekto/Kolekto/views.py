import django.core.exceptions
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Produto, Loja, Usuario
from django.http import Http404


def Registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            Usuario.objects.get(username=username)
        except:
            Usuario.objects.create(username=username, nome=nome, email=email, senha=senha)
            request.session["usuario"] = username
            return redirect(home)
        else:
            return render(request, 'registro.html', {"erro": "usuário já existe"})
    return render(request, 'registro.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        try:
            usuario = Usuario.objects.get(username=username, senha=senha)
        except:
            return render(request, 'login.html', {"erro": "usuário não encontrado"})
        else:
            request.session["usuario"] = usuario.username
            print(request.session["usuario"])
            return redirect(home)
    return render(request, 'login.html')


def Cadastro_Loja(request):
    try:
        usuario = Usuario.objects.get(username=request.session["usuario"])
    except:
        return redirect('login')
    else:
        contexto = {
            "nome_vendedor": usuario.nome
        }
        if request.method == "POST":

            erros = {}
            data_nascimento = request.POST.get("nascimento")
            Localizacao = f"{request.POST.get('cidade')}, {request.POST.get('estado')}"
            cpf = request.POST.get("cpf")
            nome_loja = request.POST.get("nome_loja")
            banner = request.POST.get("banner")
            perfil = request.POST.get("perfil")
            associado = usuario
            descricao = request.POST.get("descricao")

            if erros:
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
                    contexto["erros"] = "preencha todos os campos corretamente"
                    contexto["data_nascimento"] = data_nascimento
                    contexto["localizacao"] = request.POST.get("cidade")
                    contexto["estado"] = True
                    contexto["cpf"] = cpf
                    contexto["nome_loja"] = nome_loja
                    contexto["banner"] = banner
                    contexto["perfil"] = perfil
                    contexto["descrito"] = descricao
                    return render(request, "cadastro_loja.html", context=contexto)
        return render(request, "cadastro_loja.html", context=contexto)


def Add_Produto(request):
    try:
        usuario = Usuario.objects.get(username=request.session["usuario"])
    except:
        return redirect(Login)
    else:
        loja = usuario.loja_set.all()
        print(loja[0])
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
                foto1 = request.POST["foto1"]
                nome_produto = request.POST["nome_produto"]
                descricao = request.POST["descricao"]
                preco = request.POST["preco"]
                categoria = request.POST["select"]
                qntd = request.POST["qntd"]

                if not nome_produto or not descricao or not preco or not qntd or not foto1 or categoria == "Selecione a categoria":
                    return render(request, "add_produto.html", {'error_message': "Preencha os campos necessários", 'categorias': categorias})

                try:
                    Produto.objects.create(foto1=foto1, nome_produto=nome_produto, descricao=descricao, preco=preco, categoria=categoria,qntd=qntd, loja=loja[0])
                finally:
                    nome = loja[0].NomeLoja
                    #return redirect('pagina_produto', id_produto=Produto.id)
            return render(request, "add_produto.html", {"categorias": categorias})

       
def pagina_produto(request, id_produto):
    id_produto = Produto.objects.get(id=id_produto)
    print(id_produto)
    if id_produto is not None:

        contexto = {
            "foto1": id_produto.foto1,
            "nome_produto": id_produto.nome_produto,
            "descricao": id_produto.descricao,
            "preco": id_produto.preco,
            "categoria":id_produto.categoria,
            "qntd":id_produto.qntd       
        }
        return render(request, "pagina_produto.html", context=contexto)
    else:
        raise Http404("Produto não encontrado")

def home(request):
    contexto = {
        "nome_pesquisado": "nome_pesquisado",
    }

        #  Q(nome_produto__icontains=nome_pesquisado)
        # | Q(description__icontains=search)
        # | Q(category__title__icontains=search))

    return render(request, "home.html", context=contexto)

def pesquisa(request,nome_pesquisado):
    if request.method == "GET":
        nome_pesquisado = request.GET.get("nome_pesquisado")
        lista_produtos = Produto.objects.filter(nome_produto=nome_pesquisado)

    contexto = {
        "nome_pesquisado":nome_pesquisado,
        "lista_produtos":lista_produtos,
    }

    return render(request, "pesquisa.html", context=contexto)


def pagina_loja(request, nome_loja):
    loja = Loja.objects.get(NomeLoja=nome_loja)
    if loja is not None:
        #produtos = list(loja.produto_set.all())
        contexto = {
            "banner": loja.Banner,
            "perfil": loja.Perfil,
            "nome_loja": loja.NomeLoja,
            "localizacao": loja.Localizacao,
            "descricao": loja.descricao,
        }
        print(contexto["perfil"].url)
        return render(request, "pagina_loja.html", context=contexto)
    else:
        raise Http404("Loja não encontrada")