from pages.login_page import LoginPage
from testdata.login_data import VALID_EMAIL, VALID_PASSWORD, VALID_MOBILE, INVALID_EMAIL_FORMAT, INVALID_PASSWORD
from utils.config import ACCOUNT_URL, LOGIN_URL
from playwright.sync_api import expect


#Login with valid mobile number and valid password

def test_valid_login(page): 
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)

# Login with invalid email and valid password

def test_invalid_email_valid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_EMAIL_FORMAT, VALID_PASSWORD)

# Login with valid email and invalid password

def test_valid_email_invalid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, INVALID_PASSWORD)

# Login with invalid email and invalid password

def test_invalid_email_invalid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_EMAIL_FORMAT, INVALID_PASSWORD)

# Login with both fields blank

def test_blank_fields(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")

# Email/mobile field blank

def test_blank_email_mobile(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", VALID_PASSWORD)

# Password field blank

def test_blank_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, "")

# Invalid email format

def test_invalid_email_format(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_EMAIL_FORMAT, VALID_PASSWORD)

# Verify password is masked by default

def test_password_masked_by_default(page):
    login_page = LoginPage(page)
    login_page.navigate()
    assert login_page.is_password_masked(), "Password should be masked by default"

# Verify password visibility toggle

def test_password_visibility_toggle(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.toggle_password_visibility()
    assert not login_page.is_password_masked(), "Password should be visible after toggling visibility"
    login_page.toggle_password_visibility()
    assert login_page.is_password_masked(), "Password should be masked again after toggling visibility"

# Verify Forgot Password navigation

def test_forgot_password_navigation(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.click_forgot_password()
    assert page.url == ACCOUNT_URL, "Forgot Password link should navigate to the correct page"

# Verify Keep Me Signed In behavior

def test_keep_me_signed_in_behavior(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD, keep_signed_in=True)
    # Add assertions to verify session persistence after closing and reopening the browser


# Verify user is redirected to correct dashboard after successful login

def test_successful_login_redirect(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    # Add assertions to verify redirection to the correct dashboard page

# Verify authenticated user cannot access login page unnecessarily

def test_authenticated_user_redirect_from_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    page.goto(LOGIN_URL)
    # Add assertions to verify that authenticated user is redirected away from the login page

# Verify logout invalidates authenticated session

def test_logout_invalidates_session(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    login_page.logout()
    # Add assertions to verify that the session is invalidated after logout

# Verify protected ERP URL cannot be accessed without authentication

def test_protected_url_access_without_authentication(page):
    page.goto(ACCOUNT_URL)
    # Add assertions to verify that unauthenticated users are redirected to the login page

# Verify session behavior after browser refresh

def test_session_behavior_after_refresh(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    page.reload()
    # Add assertions to verify that the session remains valid after a browser refresh

# Verify account/session behavior after inactivity timeout

def test_session_behavior_after_inactivity_timeout(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    # Simulate inactivity timeout (e.g., wait for a specific duration)
    # Add assertions to verify that the session is invalidated after inactivity timeout

# Verify login button cannot cause duplicate login requests on repeated clicks

def test_login_button_no_duplicate_requests(page):
    login_page = LoginPage(page)
    login_page.navigate()
    # Simulate multiple rapid clicks on the login button
    # Add assertions to verify that only one login request is processed and no duplicate requests are sent
