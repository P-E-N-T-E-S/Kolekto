const INPUT_USERNAME = '#username'
const INPUT_PASSWORD = '#password'
const BUTTON_SUBMIT = ':nth-child(3) > .btn'

Cypress.Commands.add('entrar', (usuario, senha) => {
    cy.get(INPUT_USERNAME).type(usuario)
    cy.get(INPUT_PASSWORD).type(senha)
    cy.get(BUTTON_SUBMIT).click()
})