from playwright.sync_api import sync_playwright, expect
import re

def test_login_valid_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("#username", "tomsmith")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")

        expect(page).to_have_url(re.compile(r"/secure"))
        expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

        browser.close()
