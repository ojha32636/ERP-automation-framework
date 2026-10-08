#============================================================================
# Test cases for login functionality
#============================================================================

from pages.login_page import LoginPage
from testdata.login_data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, VALID_MOBILE, INVALID_EMAIL_FORMAT, INVALID_PASSWORD
from utils.config import ACCOUNT_URL, LOGIN_URL, FORGOT_PASSWORD_URL
from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage

#============================================================================
# case 1 :Login with valid mobile number and valid password
#============================================================================

def test_valid_login(page): 
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)       
    expect(page).to_have_url(ACCOUNT_URL) # this will verify user is logged in and redirected to the account page.

#=============================================================================
# End of test cases1 for login functionality
#=============================================================================
    

#=============================================================================
# case 2 :Login with invalid email and valid password.
#=============================================================================

def test_invalid_email_valid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD)
    expect(login_page.error_toast_title).to_have_text("Error") # this will verify that the error title is displayed.
    expect(login_page.error_toast_message).to_have_text("This email does not exist") # this will verify that the error message is displayed.
    expect(page).to_have_url(LOGIN_URL) # this will verify user is not logged in and remains on the login page.

#=============================================================================
# End of test cases2 for login functionality
#=============================================================================


#=============================================================================
# case 3 :Login with valid email and invalid password.
# =============================================================================    

def test_valid_email_invalid_password(page):
     login_page = LoginPage(page)
     login_page.navigate()
     login_page.login(VALID_EMAIL, INVALID_PASSWORD)
     expect(login_page.error_toast_title).to_have_text("Error") # this will verify that the error title is displayed.
     expect(login_page.error_toast_message).to_have_text("Invalid password") # this will verify that the error message is displayed.
     expect(page).to_have_url(LOGIN_URL) # this will verify user is not logged in and remains on the login page.

#=============================================================================
# End of test cases3 for login functionality
#=============================================================================

#=============================================================================
# case 4 :Login with invalid email and invalid password.
# =============================================================================

def test_invalid_email_invalid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_EMAIL, INVALID_PASSWORD)
    expect(page).to_have_url(LOGIN_URL) # this will verify user is not logged in and remains on the login page.
    expect(login_page.error_toast_title).to_have_text("Error") # this will verify that the error title is displayed.
    expect(login_page.error_toast_message).to_have_text("This email does not exist") # this will verify that the error message is displayed.
#=============================================================================
# End of test case 4 for login functionality    
#=============================================================================

#=============================================================================
# case 5 :Login with both fields blank
# =============================================================================

def test_blank_fields(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")
    expect(page).to_have_url(LOGIN_URL) # this will verify user is not logged in and remains on the login page.
    expect(login_page.error_message_email).to_have_text("Email or Mobile number is required.") # this will verify that the error title is displayed.
    expect(login_page.error_msg_password).to_have_text("Password is required.") # this will verify that the error message is displayed.
#=============================================================================
# End of test case 5 for login functionality
#============================================================================

#=============================================================================
# case 6:Email/mobile field blank
#============================================================================

def test_blank_email_mobile(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", VALID_PASSWORD)
    expect(login_page.error_message_email).to_have_text("Email or Mobile number is required.")
    expect(page).to_have_url(LOGIN_URL) # this will verify user is not logged in and remains on the login page.

#=============================================================================
# End of test case 6 for login functionality
#============================================================================

#=============================================================================
# case 7:Password field blank
#============================================================================

def test_blank_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_EMAIL, "")
    expect(login_page.error_msg_password).to_have_text("Password is required.")
    expect(page).to_have_url(LOGIN_URL) # this will verify user is not logged in and remains on the login page.

#=============================================================================
# End of test case 7 for login functionality
#============================================================================

#=============================================================================
# case 8:Invalid email format
#============================================================================

def test_invalid_email_format(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_EMAIL_FORMAT, VALID_PASSWORD)
    expect(login_page.error_message_email).to_have_text("Please enter a valid email or mobile number.")

#=============================================================================
# End of test case 8 for login functionality
#============================================================================

#==============================================================================
# case 9:Verify password is masked by default
#=============================================================================
def test_password_masked_by_default(page):
    login_page = LoginPage(page)
    login_page.navigate()
    expect(login_page.password_input).to_have_attribute("type", "password")  # this will verify that the password input field is of type "password" by default, indicating that the password is masked.

#=============================================================================
# End of test case 9 for login functionality
#============================================================================

#=============================================================================
# case 11:Verify password visibility toggle
#=============================================================================

def test_password_visibility_toggle(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.eye_icon.click()  # Click the eye icon to toggle password visibility
    expect(login_page.password_input).to_have_attribute("type", "text"), "Password should be visible after toggling visibility"
    login_page.eye_icon.click()  # Click the eye icon again to mask the password
    expect(login_page.password_input).to_have_attribute("type", "password"), "Password should be masked again after toggling visibility"

#=============================================================================
# End of test case 11 for login functionality
#============================================================================

#=============================================================================
# case 12:Verify "Forgot Password" link navigation
#=============================================================================

def test_forgot_password_navigation(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.forgot_password_link.click()  # Click the "Forgot Password" link
    expect(page).to_have_url(FORGOT_PASSWORD_URL), "Forgot Password link should navigate to the correct page"
    expect(page).to_have_title("Forgot Password - ERPNext"), "Forgot Password page should have the correct title"
#=============================================================================
# End of test case 12 for login functionality
#=============================================================================

#=============================================================================
# case 13:Verify "Keep me Signed In" checkbox behavior
#=============================================================================

def test_keep_me_signed_in_behavior(browser): 
    context_1 = browser.new_context()
    #=================================================================
    # Browser 1 - Login with "Keep me Signed In" checked
    #=================================================================
    page_1 = context_1.new_page()

    login_page = LoginPage(page_1)

    login_page.navigate()
    login_page.keep_me_signed_in.check()  # Check the "Keep Me Signed In" checkbox
    login_page.login(VALID_MOBILE, VALID_PASSWORD)
    expect(page_1).to_have_url(ACCOUNT_URL)
    
    #=================================================================
    # Browser closed
    #=================================================================
    context_1.close()

    #=================================================================
    # Browser 2 - Open a new browser context and verify user is still logged in
    #=================================================================
    context_2 = browser.new_context()
    page_2 = context_2.new_page()
    page_2.goto(LOGIN_URL)
    expect(page_2).to_have_url(ACCOUNT_URL)
    
    #=================================================================
    # Cleanup
    #=================================================================
    context_2.close()

#=============================================================================
# End of test case 13 for login functionality
#=============================================================================

#=============================================================================
# case 14:Verify user is redirected to correct dashboard after successful login
#=============================================================================
def test_successful_login_redirect(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)
    expect(page).to_have_url(ACCOUNT_URL) # this will verify that the authenticated user is redirected away from the login page to the account page.
#=============================================================================
# End of test case 14 for login functionality
#============================================================================

#=============================================================================
# case 15:Verify authenticated user cannot access login page unnecessarily
# =============================================================================

def test_authenticated_user_redirect_from_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)
    expect(page).to_have_url(ACCOUNT_URL) # this will verify that the authenticated user is redirected away from the login page to the account page.
    
    page.goto(LOGIN_URL)
    expect(page).to_have_url(ACCOUNT_URL) # this will verify that the authenticated user is redirected away from the login page to the account page.
    # print("Authenticated user is redirected away from the login page to the account page.")
#=============================================================================
# End of test case 15 for login functionality
#============================================================================

#=============================================================================
# case 16:Verify logout invalidates authenticated session
# ============================================================================

def test_logout_invalidates_session(browser):

    context = browser.new_context()

    # ==========================================
    # TAB 1 - Login
    # ==========================================

    page_1 = context.new_page()

    login_page = LoginPage(page_1)

    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)

    expect(page_1).to_have_url(ACCOUNT_URL)

    print("User is logged in and redirected to the account page.")

    # ==========================================
    # TAB 2 - Open authenticated session
    # ==========================================

    page_2 = context.new_page()

    page_2.goto(ACCOUNT_URL)

    expect(page_2).to_have_url(ACCOUNT_URL)

    print("Second tab opened with authenticated session.")

    # ==========================================
    # Switch back to TAB 1
    # ==========================================

    page_1.bring_to_front()

    print("Switched back to the first tab.")

    # ==========================================
    # Logout from TAB 1
    # ==========================================

    dashboard_page = DashboardPage(page_1)

    dashboard_page.logout()

    expect(page_1).to_have_url(LOGIN_URL)

    print("User has logged out from the first tab.")

    # ==========================================
    # Switch to TAB 2
    # ==========================================

    page_2.bring_to_front()

    # print("Switched to the second tab.")

    # ==========================================
    # Refresh TAB 2
    # ==========================================

    page_2.reload()

    #print(f"URL after refreshing second tab: {page_2.url}")

    # ==========================================
    # Verify session was invalidated
    # ==========================================

    expect(page_2).to_have_url(LOGIN_URL)

    # print(
    #     "Second tab was redirected to the login page "
    #     "after the session was invalidated."
    # )

    # ==========================================
    # Cleanup
    # ==========================================

    context.close()
    
#=============================================================================
# End of test case 16 for login functionality
# ============================================================================
  
#=============================================================================
# case 17: Verify protected ERP URL cannot be accessed without authentication
#=============================================================================

def test_protected_url_access_without_authentication(page):
    page.goto(ACCOUNT_URL)
    expect(page).to_have_url(LOGIN_URL) # this will verify that the unauthenticated user is redirected to the login page when trying to access a protected URL.
#=============================================================================
# End of test case 17 for login functionality
#=============================================================================

#=============================================================================
# case 18: Verify session behavior after browser refresh
#=============================================================================

def test_session_behavior_after_refresh(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)
    print("User is logged in and redirected to the account page.")
    page.wait_for_timeout(5000)  # Adjust the wait time as needed
    page.reload()  # Refresh the browser
    expect(page).to_have_url(ACCOUNT_URL) # this will verify that the authenticated user remains logged in and on the account page after refreshing the browser.
#=============================================================================
# End of test case 18 for login functionality
#=============================================================================

#=============================================================================
# case 19: Verify session behavior after inactivity timeout
#=============================================================================

# def test_session_behavior_after_inactivity_timeout(page):
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.login(VALID_EMAIL, VALID_PASSWORD)
#     # Simulate inactivity timeout (e.g., wait for a specific duration)
#     # Add assertions to verify that the session is invalidated after inactivity timeout

#=============================================================================
# End of test case 19 for login functionality
#=============================================================================

#=======================================================================================
# case 20: Verify login button cannot cause duplicate login requests on repeated clicks
#========================================================================================

# def test_login_button_no_duplicate_requests(page):
#     login_page = LoginPage(page)
#     login_page.navigate()
#     # Simulate multiple rapid clicks on the login button
#     # Add assertions to verify that only one login request is processed and no duplicate requests are sent

#=============================================================================
# End of test case 20 for login functionality
#=============================================================================