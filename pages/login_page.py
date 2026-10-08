from utils.config import LOGIN_URL

class LoginPage:
    
    def __init__(self, page):
        self.page = page

        #--------Elements on the Login Page--------

        #--------Input Fields for username--------
        self.username_input = page.get_by_placeholder("Enter your email or mobile number")

        #--------Input Fields for password--------
        self.password_input = page.get_by_placeholder("Enter your password")

        #--------Eye icon to toggle password visibility--------
        self.eye_icon = page.locator(".wpa_login_ic_eye")

        #--------Button to submit the login form--------
        self.login_button = page.get_by_role("button", name="Sign In")

        #--------Link to the Forgot Password page--------
        self.forgot_password_link = page.locator("a[href='/forgot-password']")

        #--------Checkbox for "Keep me Signed In" option--------
        self.keep_me_signed_in = page.locator("//label[normalize-space()='Keep me Signed In']")

        #--------Toast messages title for success--------
        self.success_toast_title = page.locator(".erp_toast_title").filter(has_text="Success")

        #--------Toast messages title for error--------
        self.error_toast_title = page.locator(".erp_toast_title").filter(has_text="Error")

        #--------Toast messages for success--------
        self.success_toast_message = page.locator(".erp_toast_message").filter(has_text="Welcome! You are logged in successfully")

        #--------Toast messages for error--------
        self.error_toast_message = page.locator(".erp_toast_message").filter(has_text="Invalid credentials")

        #--------Error message for username input field--------
        self.error_message_email = page.locator(".error_msg").filter(has_text="Email or Mobile number is required.")

        #--------Error message for password input field--------
        self.error_msg_password = page.locator(".error_msg").filter(has_text="Password is required.")


    #--------Methods to interact with the Login Page--------
    def navigate(self):
        self.page.goto(LOGIN_URL)
        
    #--------Method to submit the login form--------
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
      