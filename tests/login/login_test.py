from pages.login_page import LoginPage
from testdata.login_data import VALID_PASSWORD, VALID_MOBILE
from utils.config import ACCOUNT_URL, LOGIN_URL

#Login with valid mobile number and valid password
def test_valid_login(page): 
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_MOBILE, VALID_PASSWORD)

# Login with invalid email and valid password









# Login with valid email and invalid password

# Login with invalid email and invalid password

# Login with both fields blank

# Email/mobile field blank

# Password field blank

# Invalid email format

# Verify password is masked by default

# Verify password visibility toggle

# Verify Forgot Password navigation

# Verify Keep Me Signed In behavior

# Verify user is redirected to correct dashboard after successful login

# Verify authenticated user cannot access login page unnecessarily

# Verify logout invalidates authenticated session

# Verify protected ERP URL cannot be accessed without authentication

# Verify session behavior after browser refresh

# Verify account/session behavior after inactivity timeout

# Verify login button cannot cause duplicate login requests on repeated clicks
