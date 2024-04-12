const INPUT_FPERFIL = '#perfil'
const INPUT_NASCIMENTO = '#nascimento'
const INPUT_CPF = '#cpf'
const INPUT_NOMELOJA = '#nome_loja'
const INPUT_DESCRICAO = '#descricao'
const INPUT_CIDADE = '#RuaAvenida'
const INPUT_ESTADO = '#estado'
const BUTTON_SUBMIT = '#cadastro'
const P_TITULO_LOJA = '#erros'

Cypress.Commands.add('registrarLoja', (fotoperfil, datanascimento, cpf, nomeLoja, descricao, cidade, estado) => {
    cy.get(INPUT_FPERFIL).type(fotoperfil)
    cy.get(INPUT_NASCIMENTO).type(datanascimento)
    cy.get(INPUT_CPF).type(cpf)
    cy.get(INPUT_NOMELOJA).type(nomeLoja)
    cy.get(INPUT_DESCRICAO).type(descricao)
    cy.get(INPUT_CIDADE).type(cidade)
    cy.get(INPUT_ESTADO).select(estado)
    cy.get(BUTTON_SUBMIT).click()
})

Cypress.Commands.add('verificarNomeIgual', () => {
    cy.get(P_TITULO_LOJA).should('exist');
})
