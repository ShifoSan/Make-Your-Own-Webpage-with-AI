import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file://{os.getcwd()}/index.html')
        await page.screenshot(path='jules-scratch/verification/hero_section.png')
        details_section = page.locator('#details')
        await details_section.scroll_into_view_if_needed()
        await page.screenshot(path='jules-scratch/verification/details_section.png')
        await browser.close()

asyncio.run(main())
