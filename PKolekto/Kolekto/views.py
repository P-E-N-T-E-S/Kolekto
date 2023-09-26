from django.shortcuts import render
from .models import Produto, Loja
# Create your views here.

'''def val_cpf(num):
    num = num.split('.')
    aux = num[2].split('-')
    num.append(aux[0])
    num.append(aux[1])
    num'''
def Cadastro_Loja(request):
    contexto = {
        "nome_vendedor": "Marcílio"
    }
    if request.method == "POST":
        data_nascimento = request.POST.get("nascimento")
        Localizacao = f"{request.POST.get('cidade')}, {request.POST.get('estado')}"
        cpf = request.POST.get(("cpf"))
        nome_loja = request.POST.get("nome_loja")
        banner = request.POST.get("banner")
        perfil = request.POST.get("perfil")
        nome_vendedor = contexto["nome_vendedor"]
        Loja.objects.create(Banner=banner, Perfil=perfil, NomeLoja=nome_loja, NomeVendedor=nome_vendedor, Cpf=cpf,
                            DataNascimento=data_nascimento, Localizacao=Localizacao)


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