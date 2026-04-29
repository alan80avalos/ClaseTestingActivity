import { test, expect } from '@playwright/test';

const searchTerms = [
  'Hello, world!',
  'Iteso',
  'Amazon',
];

for (const searchTerm of searchTerms) {
  test(`Searching for "${searchTerm}" on Google`, async ({ page }) => {
    await page.goto('https://www.google.com');

    await page.waitForTimeout(10000);

    const searchBox = page.locator('[id="APjFqb"]');

    await searchBox.fill(searchTerm);

    await page.waitForTimeout(10000);

    await Promise.all([
      page.waitForURL(/search/),
      searchBox.press('Enter'),
    ]);

    await expect(page).toHaveTitle(new RegExp(`^${searchTerm}`));
  });
}