from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Launch headless browser
    page = browser.new_page()
    page.goto('https://www.facebook.com')
    print(page.title())  # Print the page title
    browser.close()
