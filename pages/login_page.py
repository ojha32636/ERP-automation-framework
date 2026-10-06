from utils.config import LOGIN_URL

class LoginPage:
    
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Enter your email or mobile number")
        self.password_input = page.get_by_placeholder("Enter your password")
        self.login_button = page.get_by_role("button", name="Sign In")

    def navigate(self):
        self.page.goto(LOGIN_URL)
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()