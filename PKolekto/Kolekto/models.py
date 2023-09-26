from django.db import models

# Create your models here.


class Loja(models.Model):
    Banner = models.ImageField(upload_to="ban_imgs/")
    Perfil = models.ImageField(upload_to="perf_imgs/")
    NomeLoja = models.CharField(max_length=30)
    NomeVendedor = models.CharField(max_length=50)
    Cpf = models.TextField(max_length=14)
    DataNascimento = models.DateTimeField()
    Localizacao = models.TextField(max_length=50)