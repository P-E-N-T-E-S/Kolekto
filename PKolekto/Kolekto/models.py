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
    
class Produto(models.Model):
    foto1 = models.ImageField(upload_to="fotos/")
    foto2 = models.ImageField(upload_to="fotos/")
    foto3 = models.ImageField(upload_to="fotos/")
    foto4 = models.ImageField(upload_to="fotos/")
    nome_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    qntd = models.PositiveSmallIntegerField()
