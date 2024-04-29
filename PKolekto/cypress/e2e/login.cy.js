describe('Checkpoint', () => {
    it('Criacao de review', () => {
        cy.visit('/')
        cy.get('[placeholder="Usuário"]').type("jota")
        cy.get('[placeholder="Senha"]').type("123")
        cy.get('.poppins-semibold').click()
        cy.get('input').type("{ENTER}")
        cy.get(':nth-child(5) > div > a > h1').click()
        //cy.get('#addReview').click()
        //cy.get('#texto').type("muito bom o jogo, joguei 3x")
        //cy.get('div > form > button').click()
        cy.get('.review').invoke('text').should('have.string', 'muito bom o jogo, joguei 3x')
    })
  })