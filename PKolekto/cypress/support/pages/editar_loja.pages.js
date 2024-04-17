const INPUT_FPERFIL = '#perfil'
const INPUT_NASCIMENTO = '#nascimento'
const INPUT_CPF = '#cpf'
const INPUT_NOMELOJA = '#nome_loja'
const INPUT_DESCRICAO = '#descricao'
const INPUT_CIDADE = '#RuaAvenida'
const INPUT_ESTADO = '.form-select'
const BUTTON_SUBMIT = '#Alterar'


Cypress.Commands.add('alterarNome', (nomeLoja, estado) => {
    cy.get(INPUT_NOMELOJA).type("{selectall}"+nomeLoja)
    cy.get(INPUT_ESTADO).select(estado)
    cy.get(BUTTON_SUBMIT).click()
})