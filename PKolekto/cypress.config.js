const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://127.0.0.1:8000",
    viewportWidth: 1920,
    viewportHeight: 1080,
    watchForFileChanges: false, //reexecuta o cenario ao salvar um arquivo, setando para false
    specPattern: "cypress/e2e/**/*.feature",
    setupNodeEvents(on, config) {
      const cucumber = require("cypress-cucumber-preprocessor").default;
      on("file:preprocessor", cucumber());
    },
  },
});
