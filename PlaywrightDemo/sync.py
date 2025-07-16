from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.youtube.com/",timeout=60000)
    page.screenshot(path="Demo.png")
    browser.close()
