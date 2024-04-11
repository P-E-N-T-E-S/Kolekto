const P_TITULO_LOJA = '.mb-0'

Cypress.Commands.add('verLoja', (nome) => {
    cy.url().should('equal', 'http://127.0.0.1:8000/minha_loja');
})