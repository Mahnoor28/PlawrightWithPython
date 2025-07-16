import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        await page.set_viewport_size({"width": 1080, "height": 1200})
        await page.goto("https://demoqa.com/select-menu")

    
        await page.select_option("select#cars", ['volvo', 'saab', 'audi'])
        await page.screenshot(path="screenshots/options.png")

     
        await context.tracing.stop(path="logs/trace2.zip")

        await browser.close()

asyncio.run(main())
