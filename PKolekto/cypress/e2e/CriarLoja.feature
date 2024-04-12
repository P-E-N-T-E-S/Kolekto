#utf-8
#language: pt

Funcionalidade: CriarLoja
    Cenário: criar loja com sucesso
        Dado que eu tenho um perfil comum de usuário no site
        Quando eu adicionar meus dados e criar um perfil de loja chamado "Minis Recife"
        Então devo conseguir entrar na pagina: minha_loja
    
    Cenário: criar loja com nome igual
        Dado que eu tenho um perfil de usuario comum
        E exista uma loja chamada "Gêmeos das Minis"
        Quando eu tentar criar uma loja chamado "Gêmeos das Minis"
        Então devo ser informado que necessito alterar o nome da loja