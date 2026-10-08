import os
import pytest_html
import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS

#=========================================================================================================================
# This section is responsible for setting up the Playwright environment and providing fixtures for browser and page objects. It also includes a hook to take screenshots on test failures.
#=========================================================================================================================

# this fixture initializes the Playwright environment and yields the Playwright object for use in tests.
@pytest.fixture
def playwright():

    with sync_playwright() as p:
        yield p

#=================================================================================================================================       
#If want to add more browsers, you can add them to the params list in the fixture below. For example, if you want to run tests on Firefox and WebKit, you can change the params list to ["chromium", "firefox", "webkit"].
#================================================================================================================================
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

# this fixture creates a new browser context and page for each test function. It yields the page object to the test function and closes the context after the test is done.
@pytest.fixture
def page(browser):  
        context = browser.new_context() #this line creates a new browser context, which is like a new browser profile. It allows you to have multiple independent sessions in the same test run.
        page = context.new_page() #this line creates a new page (or tab) in the browser context. You can use this page object to interact with the web application in your tests.

        yield page # this will return the page object to the test function.

        context.close()

#=====================================================================================================================================
#  this section is responsible for taking a screenshot when a test fails. The pytest_runtest_makereport hook is called after each test is executed, and it checks if the test has failed. If it has, it retrieves the page object from the test function's arguments and takes a screenshot of the current state of the page. The screenshot is saved in the "reports/screenshots" directory with the name of the test function.
#=====================================================================================================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = f"reports/screenshots/{item.name}.png"

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )