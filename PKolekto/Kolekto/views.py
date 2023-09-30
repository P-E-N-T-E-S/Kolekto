from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Produto, Loja, Usuario
from django.db.models import Q
# Create your views here.

def Registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = Usuario.objects.create(username=username, nome=nome, email=email, senha=senha)
        login(request, usuario)
        return redirect('home') 
    return render(request, 'registro.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, senha=senha)
        if user is not None:
            login(request, user)
            return redirect('home')  
    return render(request, 'login.html')


def Cadastro_Loja(request):
    contexto = {
        "nome_vendedor": Usuario.objects.get(login=request.session["usuario"]).nome
    }
    if request.method == "POST":

        erros = {}

        data_nascimento = request.POST.get("nascimento")
        Localizacao = f"{request.POST.get('cidade')}, {request.POST.get('estado')}"
        cpf = request.POST.get(("cpf"))
        nome_loja = request.POST.get("nome_loja")
        banner = request.POST.get("banner")
        perfil = request.POST.get("perfil")
        nome_vendedor = contexto["nome_vendedor"]
        descricao = request.POST.get("descricao")

        if not (cpf.find('.') == 3 and cpf[4:] == 3 and cpf.find("-") == 11 and len(cpf) == 14):
            erros["cpf_mask"] = "Digite o cpf corretamente"

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
            Loja.objects.create(Banner=banner, Perfil=perfil, NomeLoja=nome_loja, NomeVendedor=nome_vendedor, Cpf=cpf,
                            DataNascimento=data_nascimento, Localizacao=Localizacao, descricao=descricao)


    return render(request, "cadastro_loja.html", context=contexto)


def Add_Produto(request):
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
        foto2 = request.POST["foto2"]
        foto3 = request.POST["foto3"]
        foto4 = request.POST["foto4"]
        nome_produto = request.POST["nome_produto"]
        descricao = request.POST["descricao"]
        preco = request.POST["preco"]
        categoria = request.POST["select"]  
        qntd = request.POST["qntd"]
        
        if not nome_produto or not descricao or not preco or not qntd or not foto1 or categoria == "Selecione a categoria":
            return render(request, "add_produto.html", {'error_message': "Preencha os campos necessários", 'categorias': categorias})

        try: 
            Produto.objects.create(foto1=foto1, foto2=foto2, foto3=foto3, foto4=foto4, nome_produto=nome_produto, descricao=descricao, preco=preco, categoria=categoria,qntd=qntd)
        finally:
            return render(request, "cadastro_loja.html")
    

    return render(request, "add_produto.html", {"categorias": categorias})

def product_list(request):

    contexto = {
        "nome_pesquisado": "nome_pesquisado",
    }

    if request.method == "GET":
        nome_pesquisado = request.GET.get("nome_pesquisado")
        lista_produtos = Produto.objects.filter(nome_produto=nome_pesquisado)
        #  Q(nome_produto__icontains=nome_pesquisado)
        # | Q(description__icontains=search)
        # | Q(category__title__icontains=search))

    return render(request, "home.html", context=contexto)

def pagina_loja(request, nome_loja):
    loja = Loja.objects.get(NomeLoja = nome_loja)
    contexto = {
        "banner": loja.Banner,
        "perfil": loja.Perfil,
        "nome_loja": loja.NomeLoja,
        "localizacao": loja.Localizacao,
        "descricao": loja.descricao
    }

    return render(request, "pagina_loja.html", context=contexto)