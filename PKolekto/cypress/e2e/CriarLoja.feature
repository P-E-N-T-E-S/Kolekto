#utf-8
#language: pt

Funcionalidade: CriarLoja
    Cenário: criar loja com sucesso
        Dado que eu tenho um perfil comum de usuário no site
        Quando eu adicionar meus dados e criar um perfil de loja chamado "Minis Recife"
        Então devo conseguir entrar na pagina: minha_loja