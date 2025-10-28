// playwright.config.js
const { devices } = require('@playwright/test');

const config = {
  testDir: './jules-scratch/verification', // Explicitly point to the test directory
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
};

module.exports = config;
