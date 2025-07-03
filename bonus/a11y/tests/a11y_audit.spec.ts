
    /*
    1. Imports the @axe-core/playwright package
    2. Uses normal Playwright Test syntax to define a test case
    3. Uses normal Playwright syntax to navigate to the page under test
    4. Awaits AxeBuilder.analyze() to run the accessibility scan against the page
    5. Uses normal Playwright Test assertions to verify that there are no violations in the returned scan results
    */

import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright'; // 1

const PAGE_URL = 'https://languagewire.com'

test.describe('homepage', () => { // 2
  test('should not have any automatically detectable accessibility issues', async ({ page }) => {
    await page.goto(PAGE_URL); // 3

    const accessibilityScanResults = await new AxeBuilder({ page }).analyze(); // 4

   expect(accessibilityScanResults.violations).toEqual([]); // 5
  });
});

test('should not have any automatically detectable WCAG A or AA violations', async ({ page }) => {
  await page.goto(PAGE_URL);

  const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});