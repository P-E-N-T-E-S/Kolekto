from django.shortcuts import render
from .models import Produto
# Create your views here.

def Cadastro_Loja(request):
    if request.method == "POST":
        cidade = request.POST.get("cidade", None)
        print(cidade)

    contexto = {
        "nome_vendedor": "Marcílio"
    }
    return render(request, "cadastro_loja.html", context=contexto)

def Add_Produto(request):
    categorias = [
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
        
        if not nome_produto or not descricao or not preco or not qntd or not foto1:
            return render(request, "add_produto.html", {'error_message': "Preencha os campos necessários", 'categorias': categorias})

        try: 
            Produto.objects.create(foto1=foto1, foto2=foto2, foto3=foto3, foto4=foto4, nome_produto=nome_produto, descricao=descricao, preco=preco, categoria=categoria,qntd=qntd)
        finally:
            return render(request, "cadastro_loja.html")
    

    return render(request, "add_produto.html", {"categorias": categorias})
