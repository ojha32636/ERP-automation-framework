import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS

@pytest.fixture
def playwright():

    with sync_playwright() as p:
        yield p
#If want to add more browsers, you can add them to the params list in the fixture below. For example, if you want to run tests on Firefox and WebKit, you can change the params list to ["chromium", "firefox", "webkit"].

@pytest.fixture(params=["chromium"])
def browser(request):

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

        yield browser

        browser.close()

@pytest.fixture
def page(browser):  
        context = browser.new_context() #this line creates a new browser context, which is like a new browser profile. It allows you to have multiple independent sessions in the same test run.
        page = context.new_page() #this line creates a new page (or tab) in the browser context. You can use this page object to interact with the web application in your tests.

        yield page # this will return the page object to the test function.

        context.close()
        