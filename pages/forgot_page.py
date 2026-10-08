from pages.login_page import LoginPage
from utils.config import FORGOT_PASSWORD_URL, LOGIN_URL

class ForgotPasswordPage:
    def __init__(self, page):
        self.page = page
        
        #--------Elements on the Forgot Password Page--------
       
        #--------Input Field for email--------
        self.email_input = page.get_by_placeholder("you@example.com")

        #--------Button to submit the forgot password request--------
        self.submit_button = page.get_by_role("button", name="Send reset link")

        #--------Link to go back to the login page--------
        self.back_to_login_link = page.locator("//a[normalize-space()='Back to sign in']")

        #--------Messages for success--------
        self.success_toast_title = page.locator(".sa-login-box").filter(has_text="Check Your Email")

        #--------Messages for error--------
        self.error_toast_title = page.locator(".erp_toast_title").filter(has_text="Error")

        #--------Messages for success--------
        self.success_toast_message = page.locator(".sa-hint").filter(has_text="If that address belongs to an account, a reset link is on its way. The link expires in 60 minutes and can be used once.")

        #--------Messages for error--------
        self.error_toast_message = page.locator(".erp_toast_message").filter(has_text="Email not found.")

        #--------Error message for empty email input field--------
        self.empty_error_message_email = page.locator("//div[@class='sa-help']").filter(has_text="Email is required.")
       
        #--------Error message for invalid email input field--------
        self.error_message_invalid_email = page.locator("//div[@class='sa-help']").filter(has_text="Enter a valid email address.")
    
    #--------Methods to access the Forgot Password Page--------
    
    def navigate(self):
        self.page.goto(FORGOT_PASSWORD_URL)

    #--------Method to submit the forgot password request--------
    def submit_forgot_password(self, email):
        self.email_input.fill(email)
        self.submit_button.click()

    #--------Method to go back to the login page--------
    def back_to_login(self):
        self.back_to_login_link.click()
