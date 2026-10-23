from pages.side_menu import NavBar
from playwright.sync_api import expect
from fixtures.loggedin_page import logged_in

# Case 1: Verify Items page heading and breadcrumb navigation

def test_verify_items_page_heading_and_breadcrumb_navigation(logged_in):
    navigation = NavBar(logged_in)
    
    navigation.inv_items()





