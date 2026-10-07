from utils.config import LOGIN_URL

class LoginPage:
    
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Enter your email or mobile number")
        self.password_input = page.get_by_placeholder("Enter your password")
        self.eye_icon = page.locator(".wpa_login_ic_eye")
        self.login_button = page.get_by_role("button", name="Sign In")
        self.forgot_password_link = page.locator("a[href='/forgot-password']")
        self.keep_me_signed_in = page.locator("//label[normalize-space()='Keep me Signed In']")
        self.success_toast_title = page.locator(".erp_toast_title").filter(has_text="Success")
        self.error_toast_title = page.locator(".erp_toast_title").filter(has_text="Error")
        self.success_toast_message = page.locator(".erp_toast_message").filter(has_text="Welcome! You are logged in successfully")
        self.error_toast_message = page.locator(".erp_toast_message").filter(has_text="Invalid credentials")
        self.error_message_email = page.locator(".error_msg").filter(has_text="Email or Mobile number is required.")
        self.error_msg_password = page.locator(".error_msg").filter(has_text="Password is required.")


    def navigate(self):
        self.page.goto(LOGIN_URL)
        

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
      