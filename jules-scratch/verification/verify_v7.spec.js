const { test, expect } = require('@playwright/test');

test.describe('V7 "Ambient Drift" Verification', () => {
  let browser;
  let context;
  let page;
  let consoleErrors = [];

  test.beforeAll(async ({ playwright }) => {
    browser = await playwright.chromium.launch();
  });

  test.afterAll(async () => {
    await browser.close();
  });

  test.beforeEach(async () => {
    context = await browser.newContext();
    page = await context.newPage();
    consoleErrors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') {
        consoleErrors.push(msg.text());
      }
    });
    await page.goto('http://localhost:8080');
  });

  test.afterEach(async () => {
    await context.close();
  });

  test('1. No Console Errors', () => {
    expect(consoleErrors).toEqual([]);
  });

  test('2. Smooth Animation (Visual Check & Screenshot)', async () => {
    await page.waitForTimeout(2000);
    await page.screenshot({ path: 'jules-scratch/verification/v7_ambient_drift.png' });
  });

  test('3. Z-Index Check', async () => {
    const headingZIndex = await page.evaluate(() => {
        const heroContent = document.querySelector('.hero-content');
        return window.getComputedStyle(heroContent).zIndex;
    });
    const orbZIndex = await page.evaluate(() => {
        const orb = document.querySelector('.builder-orb-container');
        return window.getComputedStyle(orb).zIndex;
    });

    const shapeZIndex = await page.evaluate(() => {
        const shape = document.querySelector('.hero-shapes');
        return window.getComputedStyle(shape).zIndex;
    });

    expect(parseInt(shapeZIndex)).toBeLessThan(parseInt(headingZIndex));
    expect(parseInt(shapeZIndex)).toBeLessThan(parseInt(orbZIndex));
  });

  test('4. No Horizontal Overflow', async () => {
    const hasHorizontalOverflow = await page.evaluate(() => {
      return document.documentElement.scrollWidth > document.documentElement.clientWidth;
    });
    expect(hasHorizontalOverflow).toBe(false);
  });
});
