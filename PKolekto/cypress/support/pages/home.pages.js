const BOTAO_ACESSA_LOGIN = 'buttom:contains(Entrar)'

Cypress.Commands.add('acessaLogin', () => {
    cy.get(BOTAO_ACESSA_LOGIN).click()
})



Cypress.Commands.add('acessarCriarLoja', () => {
    cy.visit("/nova_loja")
})

Cypress.Commands.add('verHome', () => {
    cy.url().should('equal', 'http://127.0.0.1:8000');
})
