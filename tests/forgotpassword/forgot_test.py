#=========================================================================================================================
# Test case for forgot password functionality
#=========================================================================================================================
import pytest
from dotenv import load_dotenv
load_dotenv()
from pages.forgot_page import ForgotPasswordPage
from utils.config import FORGOT_PASSWORD_URL, LOGIN_URL
from utils.email_service import EmailService
from playwright.sync_api import expect
from testdata.login_data import VALID_EMAIL, INVALID_EMAIL_FORMAT, INVALID_EMAIL, EMAIL_WITH_SPACE

#==========================================================================================================================
#   Test case 1: Verify that the forgot password page loads corretly
#==========================================================================================================================
@pytest.mark.smoke
def test_verify_title(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    expect(page).to_have_title("Forgot Password | ERPNX")
#==========================================================================================================================
#   Test case 2: Submit a reset request using a registered email
#==========================================================================================================================
@pytest.mark.smoke
@pytest.mark.e2e
def test_working_with_valid_email(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.submit_forgot_password(VALID_EMAIL)
    expect(forgot_password.success_toast_title).to_have_text("Check Your Email")
    expect(forgot_password.success_toast_message).to_have_text("If that address belongs to an account, a reset link is on its way. The link expires in 60 minutes and can be used once.")
#==========================================================================================================================
#   Test case 3: Submit a reset request using an unregistered email
#==========================================================================================================================
@pytest.mark.smoke
def test_working_witth_unregistered_email(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.submit_forgot_password(INVALID_EMAIL)
    page.wait_for_timeout(3000)
    expect(forgot_password.success_toast_message).to_have_text("If that address belongs to an account, a reset link is on its way. The link expires in 60 minutes and can be used once.")


#==========================================================================================================================
#   Test case 4: Submit the form with the email field empty
#==========================================================================================================================
@pytest.mark.smoke
def test_blank_email(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.submit_forgot_password("")
    expect(forgot_password.empty_error_message_email).to_have_text("Email is required.")

#==========================================================================================================================
#   Test case 5: Enter an invalid email format
#==========================================================================================================================
@pytest.mark.smoke
def test_invalid_email_behaviour(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.submit_forgot_password(INVALID_EMAIL_FORMAT)
    expect(forgot_password.error_message_invalid_email).to_have_text("Enter a valid email address.")

#==========================================================================================================================
# Test case 6: Enter an email with leading/trailing spaces
#==========================================================================================================================
@pytest.mark.smoke

def test_email_with_space(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.submit_forgot_password(EMAIL_WITH_SPACE)
    expect(forgot_password.success_toast_title).to_have_text("Check Your Email")
    expect(forgot_password.success_toast_message).to_have_text("If that address belongs to an account, a reset link is on its way. The link expires in 60 minutes and can be used once.")


#========================================================================================================================
# Test case 8: Verify Send Reset Link button behavior
#========================================================================================================================
@pytest.mark.smoke



#====================================================================================================================
# Test case 10: Verify Back to sign in navigation
#====================================================================================================================
@pytest.mark.smoke
def test_back_to_sign_in_link(page):
    forgot_password = ForgotPasswordPage(page)
    forgot_password.navigate()
    forgot_password.back_to_login_link.click()
    expect(page).to_have_url(LOGIN_URL)
    expect(page).to_have_title("Login | ERPNX")

#====================================================================================================================
# Test case 11: Verify reset request does not reveal whether an email is registered
#====================================================================================================================
@pytest.mark.regression

#======================================================================================================================
# Test case 12: Verify multiple reset requests are handled safely
#=====================================================================================================================
@pytest.mark.regression

#=====================================================================================================================
# Test case 13: Verify reset link is delivered to the registered email
#====================================================================================================================
@pytest.mark.regression
@pytest.mark.e2e

def test_reset_link_on_email(page):
    forgot_password = ForgotPasswordPage(page)
    email_service = EmailService()
    forgot_password.navigate()
    forgot_password.submit_forgot_password(VALID_EMAIL)

    # wait and check for reset link
    email = email_service.wait_for_reset_email(
        recipient=VALID_EMAIL
    )
    reset_url = email_service.extract_reset_url(email)
    
    # 3. Open the actual reset link
    page.goto(reset_url)
    print(reset_url)





#=====================================================================================================================
# Test case 14: Verify reset link expires after its configured validity period
#======================================================================================================================
@pytest.mark.regression


#=======================================================================================================================
# Test case 15: Verify an expired or invalid reset token is rejected
#========================================================================================================================
@pytest.mark.regression

#====================================================================================================================
# Test case 16: Verify a reset token cannot be reused after successful password reset
#====================================================================================================================
@pytest.mark.regression

#====================================================================================================================
# Test case 17: Verify the new password works after reset
#===================================================================================================================
@pytest.mark.regression

#===============================================================================================================
# Test case 18: Verify the old password no longer works after reset
#==============================================================================================================
@pytest.mark.e2e
@pytest.mark.regression
#========================================================================================================
# Test case 19: Verify reset request behavior under repeated clicks
#============================================================================================================
@pytest.mark.regression

#==============================================================================================================
# Test case 20: Verify reset page behavior on browser refresh
#=============================================================================================================
@pytest.mark.regression
def reset_page_on_refresh(page):
    pass