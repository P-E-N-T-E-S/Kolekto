const P_TITULO_LOJA = '[name = "tituloLoja"]'

Cypress.Commands.add('verLoja', () => {
    cy.url().should('equal', 'http://127.0.0.1:8000/minha_loja');
})

Cypress.Commands.add('verNome', (nome) => {
    cy.get(P_TITULO_LOJA).should('have.text', nome)
})