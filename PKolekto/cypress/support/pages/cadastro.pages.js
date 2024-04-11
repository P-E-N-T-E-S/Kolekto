const INPUT_LOGIN = '#username'
const INPUT_NOME = '#nome'
const INPUT_EMAIL = '#email'
const INPUT_SENHA = '#password'
const BUTTON_SUBMIT = ':nth-child(3) > .btn'

Cypress.Commands.add('cadastrar', (usuario, nome, email, senha) => {
    cy.get(INPUT_LOGIN).type(usuario)
    cy.get(INPUT_NOME).type(nome)
    cy.get(INPUT_EMAIL).type(email)
    cy.get(INPUT_SENHA).type(senha)
    cy.get(BUTTON_SUBMIT).click()
})