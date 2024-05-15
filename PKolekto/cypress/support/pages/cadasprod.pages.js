const INPUT_FOTO = '#foto1'
const INPUT_NOME = '#nome_produto'
const INPUT_DESCRICAO = '#descricao'
const INPUT_PRECO = '#preco'
const INPUT_QUANTIDADE = '#qntd'
const SELECT_CATEGORIA = '#categoria'
const BUTTON_SUBMIT = '.continue-button > button'

Cypress.Commands.add('cadastroProduto', (foto, nome, descricao, preco, quantidade, categoria) => {
    cy.get(INPUT_FOTO).type(foto)
    cy.get(INPUT_NOME).type(nome)
    cy.get(INPUT_DESCRICAO).type(descricao)
    cy.get(INPUT_PRECO).type(preco)
    cy.get(INPUT_QUANTIDADE).type(quantidade)
    cy.get(SELECT_CATEGORIA).select(categoria)
    cy.get(BUTTON_SUBMIT).click()
})