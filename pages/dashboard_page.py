# Dashboard Page Class
from pages.login_page import LoginPage



class DashboardPage(LoginPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.profile_icon = page.locator(".erp_ad_profile")
        self.logout_link = page.locator("//a[normalize-space()='Logout']")

    def logout(self):
        # Implementation for logout functionality
        self.profile_icon.hover()  # Hover over the profile icon to reveal the dropdown menu
        self.logout_link.click()

        pass