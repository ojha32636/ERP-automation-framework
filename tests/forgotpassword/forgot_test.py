#=========================================================================================================================
# Test case for forgot password functionality
#=========================================================================================================================
from pages.forgot_page import ForgotPasswordPage
from utils.config import FORGOT_PASSWORD_URL
from playwright.sync_api import expect
from testdata.login_data import VALID_EMAIL, INVALID_EMAIL_FORMAT, INVALID_EMAIL

#==========================================================================================================================
#   Test case 2: Verify that the forgot password page has the correct title and elements
#==========================================================================================================================
def test_verify_title(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    expect(page).to_have_title("Forgot Password | ERPNX")
#==========================================================================================================================
#   Test case 3: Verify that the forgot password functionality works with valid email
#==========================================================================================================================
def test_working_with_valid_email(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.submit_forgot_password(VALID_EMAIL)
    expect(forgot_password.success_toast_title).to_be_visible()
    expect(forgot_password.success_toast_message).to_be_visible()
#==========================================================================================================================
#   Test case 4: Verify that the forgot password functionality shows an error for unregistered email
#==========================================================================================================================

#==========================================================================================================================
#   Test case 5: Verify that the forgot password functionality shows an error for invalid email format
#==========================================================================================================================

#==========================================================================================================================
#   Test case 6: Verify that the forgot password functionality shows an error for blank email
#==========================================================================================================================

#==========================================================================================================================
# Test case 7: Verify that the back to login link works
#==========================================================================================================================
