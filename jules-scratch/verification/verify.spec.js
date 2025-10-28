const { test, expect, devices } = require('@playwright/test');

test.describe('Visual Verification', () => {
  test('Hero Section - Desktop', async ({ page }) => {
    await page.goto('file:///app/index.html');
    await page.screenshot({ path: 'jules-scratch/verification/hero_section.png' });
  });

  test('Showcase Section - Mobile', async ({ page }) => {
    await page.setViewportSize(devices['iPhone 11'].viewport);
    await page.goto('file:///app/index.html');
    await page.evaluate(() => {
      document.getElementById('showcase').scrollIntoView();
    });
    await page.waitForTimeout(500); // Wait for scroll and animations
    await page.screenshot({ path: 'jules-scratch/verification/showcase_mobile.png' });
  });
});
