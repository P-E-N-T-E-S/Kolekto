from django.shortcuts import render

# Create your views here.

def Cadastro_Loja(request):
    return render(request, "cadastro_loja.html")