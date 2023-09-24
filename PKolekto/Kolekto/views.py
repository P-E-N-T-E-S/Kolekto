from django.shortcuts import render
from .forms import FormLoja

# Create your views here.

def Cadastro_Loja(request):

    form = FormLoja()
    context ={
        "form": form
    }

    return render(request, "cadastro_loja.html", context=context)