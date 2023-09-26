from django.shortcuts import render
from .models import Produto
# Create your views here.

def Cadastro_Loja(request):
    contexto ={
        "nome_vendedor": "marças"
    }
    return render(request, "cadastro_loja.html", context=contexto)

def Add_Produto(request):
    if request.method == "POST":
        foto1 = request.POST["foto1"]
        foto2 = request.POST["foto2"]
        foto3 = request.POST["foto3"]
        foto4 = request.POST["foto4"]
        nome_produto = request.POST["nome_produto"]
        descricao = request.POST["descricao"]
        preco = request.POST["preco"]

        Produto.objects.create(foto1=foto1, foto2=foto2, foto3=foto3, foto4=foto4, nome_produto=nome_produto, descricao=descricao, preco=preco)
        return render(request, "add_produto.html")
    else:
        return render(request, "add_produto.html")