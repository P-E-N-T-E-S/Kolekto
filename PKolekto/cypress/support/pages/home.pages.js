

Cypress.Commands.add('verHome', () => {
    cy.url().should('equal', 'http://127.0.0.1:8000');
})
