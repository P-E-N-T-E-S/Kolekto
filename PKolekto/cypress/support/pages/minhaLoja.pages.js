const P_TITULO_LOJA = '[name = "tituloLoja"]'
const H5_PRODUTO = '.card-title'

Cypress.Commands.add('verLoja', () => {
    cy.url().should('equal', 'http://127.0.0.1:8000/minha_loja');
})

Cypress.Commands.add('verNome', (nome) => {
    cy.get(P_TITULO_LOJA).should('have.text', nome)
})

Cypress.Commands.add('verProduto', (nome) => {
    cy.get(H5_PRODUTO).should('have.text', nome)
})