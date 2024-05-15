//Cenario 1
Given('que eu ja tenho um cadastro como vendedor e não tenho nenhu produto cadastrado', () => {
    cy.visit('/registro')
    cy.cadastrar('teste21', 'Joao', 'teste13@gmail.com', '12345')
    cy.visit('/nova_loja')
    cy.registrarLoja('https://i.imgur.com/stU4wdD.jpeg', '2003-08-29', '695.295.840-16', 'Brinquedos do Futuro', 'Descricao', 'Recife', 'Pernambuco')
})
When('eu adicionar um produto chamado "Charizard 1999 - 1º Edição", no valor de R$ 1.700.000,00 na categoria "cartas"', () => {
    cy.visit('/add_produto')
    cy.cadastroProduto('https://i.imgur.com/stU4wdD.jpeg', 'Charizard 1999 - 1º Edição', 'carta pokemon', '17000000', '1', 'Cartas')
})
Then('ao acessar o perfil da minha loja, o item “Charizard 1999 - 1º Edição” deve ser o único a aparecer no meu catálogo como vendedor.', () => {
    cy.visit('/minha_loja')
    cy.verProduto('Charizard 1999 - 1º Edição')
})