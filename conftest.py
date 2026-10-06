import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS


@pytest.fixture(params=["chromium", "firefox", "webkit"])
def page(request):

    browser_name = request.param
    
    with sync_playwright() as p:
        
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=HEADLESS)

        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=HEADLESS)

        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=HEADLESS)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()