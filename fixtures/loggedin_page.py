# this page will be used to remain logged in for after login tests.
import pytest
from pages.login_page import LoginPage
from testdata.login_data import VALID_PASSWORD, VALID_MOBILE
from utils.config import BASE_URL


@pytest.fixture
def logged_in(page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(VALID_MOBILE, VALID_PASSWORD)

    return page