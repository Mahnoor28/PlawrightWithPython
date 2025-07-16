import asyncio
from playwright.async_api import async_playwright
 
async def main():
    async with async_playwright() as p:
         browser = await p.chromium.launch(headless=False)
         page = await browser.new_page()
         await page.goto("https://www.youtube.com/", timeout=60000)
         await page.screenshot(path="Demo.png")
         await browser.close()
asyncio.run(main())