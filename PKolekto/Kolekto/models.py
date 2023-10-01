from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome = models.CharField(max_length=70)
    def __str__(self):
        return (self.username)
    
    
class Loja(models.Model):
    Banner = models.ImageField(upload_to="ban_imgs/")
    Perfil = models.ImageField(upload_to="perf_imgs/")
    NomeLoja = models.CharField(max_length=30)
    Cpf = models.CharField(max_length=14)
    DataNascimento = models.DateTimeField()
    Localizacao = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200, default="Sem dados de contato")
    associado = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return (self.NomeLoja)

    
class Produto(models.Model):
    categorias = [
        (None, "Selecione a categoria"),
        ("moveis","Móveis e Decoração"),
        ("arte","Arte"),
        ("joias","Joalheria"),
        ("livros","Livros"),
        ("relogios","Relógios"),
        ("cartas","Cartas"),
        ("brinquedos","Brinquedos e Jogos"),
        ("roupa","Vestuário"),
        ("foto","Fotografia"),
        ("musica","Instrumento Musical"),
        ("outro","Outro")
            ]
    foto1 = models.ImageField(upload_to="fotos/")
    nome_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    categoria = models.CharField(choices=categorias,default=categorias[0],max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qntd = models.PositiveSmallIntegerField()
    loja = models.ForeignKey(Loja, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return (self.nome_produto)
