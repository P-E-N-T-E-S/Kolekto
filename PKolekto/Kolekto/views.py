from django.shortcuts import render

# Create your views here.

def Cadastro_Loja(request):
    contexto ={
        "nome_vendedor": "marças"
    }
    return render(request, "cadastro_loja.html", context=contexto)