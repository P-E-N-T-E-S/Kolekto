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


def validar_cpf(cpf, validacao):
    if not validacao:
        if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
            cpf_numerico = ''.join(filter(str.isdigit, cpf))
            if len(cpf_numerico) != 11:
                return True
            if cpf_numerico == cpf_numerico[0] * 11:
                return True
            soma = 0
            for i in range(9):
                soma += int(cpf_numerico[i]) * (10 - i)
            resto = soma % 11
            digito_verificador1 = 0 if resto < 2 else 11 - resto
            if digito_verificador1 != int(cpf_numerico[9]):
                return True
            soma = 0
            for i in range(10):
                soma += int(cpf_numerico[i]) * (11 - i)
            resto = soma % 11
            digito_verificador2 = 0 if resto < 2 else 11 - resto
            if digito_verificador2 != int(cpf_numerico[10]):
                return True
            return False
        else:
            return True
    else:
        return True
