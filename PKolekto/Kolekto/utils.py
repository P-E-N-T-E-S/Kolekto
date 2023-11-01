from .views import Loja

#validações
def nomeLojaExiste(nome_loja, validacao):
    if Loja.objects.filter(NomeLoja=nome_loja).exists() or validacao:
        return True
    else:
        return False

def validacaoLinks(link, validacao):
    if link[-4:-1] != ".jp" or link[-5:-1] != ".jpe" or validacao:
        return True


#def validacaocpf()