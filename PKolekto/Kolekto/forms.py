from django import forms
from Kolekto.models import Loja

class FormLoja(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ["Banner", "Perfil", "NomeLoja", "Cpf", "DataNascimento", "Localizacao"]
