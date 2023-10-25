from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    nome = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return (self.username)
    
    
class Loja(models.Model):
    Banner = models.CharField(max_length=100)
    Perfil = models.CharField(max_length=100)
    NomeLoja = models.CharField(max_length=30)
    Cpf = models.CharField(max_length=14)
    DataNascimento = models.DateTimeField()
    Localizacao = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200, default="Sem dados de contato")
    associado = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (self.NomeLoja)

    
class Produto(models.Model):
    categorias = [
        (None, "Selecione a categoria"),
        ("Móveis e Decoração","Móveis e Decoração"),
        ("Arte","Arte"),
        ("Joalheria","Joalheria"),
        ("Livros","Livros"),
        ("Relógios","Relógios"),
        ("Cartas","Cartas"),
        ("Brinquedos e Jogos","Brinquedos e Jogos"),
        ("Vestuário","Vestuário"),
        ("Fotografia","Fotografia"),
        ("Instrumento Musical","Instrumento Musical"),
        ("Outro","Outro")
            ]
    foto1 = models.CharField(max_length=100)
    nome_produto = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    categoria = models.CharField(choices=categorias,default=categorias[0],max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qntd = models.PositiveSmallIntegerField()
    loja = models.ForeignKey(Loja, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return (self.nome_produto)
    

class ListaDesejos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)
