// Arrange - setup initial app state
// - visit a web page
// - query for an element
// Act - take an action
// - interact with the element
// Assert - make an assertion
// - make an assertion about page content

/// <reference types="Cypress" />

describe('My First Test', function() {
    it('Visits the Robin Login Page', function () {
        cy.visit('https://dashboard.robinpowered.com/ai-london/login');

        cy.wait(5000); 

        cy.get('button[id="cky-btn-accept"]').click();

        cy.get('input[id="user"]').type('username').should('have.value', 'username');

        cy.get('input[id="pass"]').type('password').should('have.value', 'password');

        cy.get('input[type="submit"]').click();

        // cy.wait(10000);

        // cy.get('input[placeholder="MM/DD/YYYY"]').then(elem => {
        //     elem.val('Mar 30');
        // });
    })
})