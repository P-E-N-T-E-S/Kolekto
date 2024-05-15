#utf-8
#language: pt

Funcionalidade: Cadastrar produto para venda
    Cenário: cadastro com sucesso
        Dado que eu ja tenho um cadastro como vendedor e não tenho nenhu produto cadastrado
        Quando eu adicionar um produto chamado "Charizard 1999 - 1º Edição", no valor de R$ 1.700.000,00 na categoria "cartas"
        Então ao acessar o perfil da minha loja, o item “Charizard 1999 - 1º Edição” deve ser o único a aparecer no meu catálogo como vendedor.