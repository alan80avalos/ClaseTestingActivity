import { test, expect } from '@playwright/test';

const searchTerms = [
  'Hello, world!',
  'Iteso',
  'Amazon',
];

for (const searchTerm of searchTerms) {
  test(`Searching for "${searchTerm}" on Bing`, async ({ page }) => {
    await page.goto('https://www.bing.com');

    await page.waitForTimeout(1000);

    const searchBox = page.locator('[id="sb_form_q"]');

    await searchBox.fill(searchTerm);

    await page.waitForTimeout(1000);

    await Promise.all([
      page.waitForURL(/search/),
      searchBox.press('Enter'),
    ]);

    await expect(page).toHaveTitle(new RegExp(`^${searchTerm}`, 'i'));
  });
}