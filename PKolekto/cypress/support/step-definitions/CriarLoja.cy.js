const { And } = require("cypress-cucumber-preprocessor/lib/resolveStepDefinition")
//Cenario 1
Given('que eu tenho um perfil comum de usuário no site', () => {
    cy.visit('/registro')
    cy.cadastrar('teste11', 'Joao', 'teste11@gmail.com', '12345')
})
When('eu adicionar meus dados e criar um perfil de loja chamado "Minis Recife"', () => {
    cy.visit('/nova_loja')
    cy.registrarLoja('https://i.imgur.com/stU4wdD.jpeg', '2003-08-29', '695.295.840-16', 'Minis Recife', 'Descricao', 'Recife', 'Pernambuco')
})
Then('devo conseguir entrar na pagina: minha_loja', () =>{
    cy.visit('/minha_loja')
    cy.verLoja()
})
//Cenario 2
Given('que eu tenho um perfil de usuario comum', () => {
    cy.visit('/registro')
    cy.cadastrar('teste12', 'Joao', 'teste12@gmail.com', '12345')
})
And('exista uma loja chamada "Gêmeos das Minis"', () => {
    cy.visit('/registro')
    cy.cadastrar('figurante121', 'Joao', 'teste121@gmail.com', '12345')
    cy.visit('/nova_loja')
    cy.registrarLoja('https://i.imgur.com/stU4wdD.jpeg', '2003-08-29', '695.295.840-16', 'Gêmeos das Minis', 'Descricao', 'Recife', 'Pernambuco')
    cy.visit('/logout')
})
When('eu tentar criar uma loja chamado "Gêmeos das Minis"', () => {
    cy.visit('/login')
    cy.entrar('teste12', '12345')
    cy.visit('/nova_loja')
    cy.registrarLoja('https://i.imgur.com/stU4wdD.jpeg', '2003-08-29', '695.295.840-16', 'Gêmeos das Minis', 'Descricao', 'Recife', 'Pernambuco')
})
Then('devo ser informado que necessito alterar o nome da loja', () => {
    cy.verificarNomeIgual()
})
//Cenario 3
Given('que eu sou um usuário sem cadastro', () => {
    cy.visit('/logout')
})
When('eu tento criar uma loja "Moedas Antigas"', () => {
    cy.visit('/nova_loja')
})
Then('eu devo ser direcionado para pagina de login', () =>{
    cy.verLoginNL()
})
//Cenario 4
Given('que eu tenho um perfil de loja criado chamado "Brinquedos do Futuro"',() => {
    cy.visit('/registro')
    cy.cadastrar('teste13', 'Joao', 'teste13@gmail.com', '12345')
    cy.visit('/nova_loja')
    cy.registrarLoja('https://i.imgur.com/stU4wdD.jpeg', '2003-08-29', '695.295.840-16', 'Brinquedos do Futuro', 'Descricao', 'Recife', 'Pernambuco')
})
When('eu edito as informações da minha loja, e troco o nome para "Relíquias do Passado"', () => {
    cy.visit('/editar/Brinquedos%20do%20Futuro')
    cy.alterarNome('Relíquias do Passado', 'Pernambuco')
})
Then('o novo nome da minha loja deve ser "Relíquias do Passado"', () => {
    cy.verNome('Relíquias do Passado')
})