const INPUT_USERNAME = '#username'
const INPUT_PASSWORD = '#password'
const BUTTON_SUBMIT = ':nth-child(3) > .btn'

Cypress.Commands.add('entrar', (usuario, senha) => {
    cy.get(INPUT_USERNAME).type(usuario)
    cy.get(INPUT_PASSWORD).type(senha)
    cy.get(BUTTON_SUBMIT).click()
})

Cypress.Commands.add('verLoginNL', () => {
    cy.url().should('equal', 'http://127.0.0.1:8000/login?next=/nova_loja')
})