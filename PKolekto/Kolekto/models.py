from django.db import models
from cpf_field.models import CPFField
from cep.models import Cep

# Create your models here.
class Loja(models.Model):
    Banner = models.ImageField(upload_to="ban_imgs/")
    Perfil = models.ImageField(upload_to="perf_imgs/")
    NomeLoja = models.CharField(max_length=30)
    NomeVendedor = models.CharField(max_length=50)
    Cpf = CPFField("cpf")
    DataNascimento = models.DateTimeField()
    #Localizacao = Cep()