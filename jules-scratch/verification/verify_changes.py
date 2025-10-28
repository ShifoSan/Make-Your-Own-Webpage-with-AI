import asyncio
from playwright.async_api import async_playwright, Page, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Set a desktop viewport for the hero section screenshot
        await page.set_viewport_size({"width": 1280, "height": 800})
        await page.goto("file:///app/index.html")
        await page.screenshot(path="jules-scratch/verification/hero_section.png")

        # Set a mobile viewport for the showcase section screenshot
        await page.set_viewport_size({"width": 375, "height": 667})
        await page.goto("file:///app/index.html#showcase")
        # Wait for the showcase section to be visible
        await page.wait_for_selector('#showcase')
        await page.screenshot(path="jules-scratch/verification/mobile_showcase.png")

        await browser.close()

asyncio.run(main())
