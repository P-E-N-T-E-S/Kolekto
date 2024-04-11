Given('que eu tenho um perfil comum de usuário no site', () => {
    cy.visit('/registro')
    cy.cadastrar('teste1', 'Joao', 'teste1@gmail.com', '12345')
})
When('eu adicionar meus dados e criar um perfil de loja chamado "Minis Recife"', () => {
    cy.visit('/nova_loja')
    cy.registrarLoja('https://i.imgur.com/stU4wdD.jpeg', '2003-08-29', '695.295.840-16', 'Minis Recife', 'Descricao', 'Recife', 'Pernambuco')
})
Then('devo conseguir entrar na pagina: minha_loja', () =>{
    cy.visit('/minha_loja')
    cy.verLoja()
})