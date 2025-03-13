from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestLocators.locators import SauceLocators
class HomePageLocators:
    """Page Object Model for the Home Page (After Login)"""

    def __init__(self, driver):
        self.driver = driver
        self.menu_button = SauceLocators.MENU_BUTTON
        self.logout_button = SauceLocators.LOGOUT_BUTTON
        self.login_button = SauceLocators.LOGIN_BUTTON
        self.cart_button = SauceLocators.CART_BUTTON

    def click_menu(self):
        """Click the menu button to open the sidebar"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

    def click_logout(self):
        """Click the logout button from the sidebar"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

    def is_logout_button_visible(self):
        """Check if the logout button is visible in the menu"""
        self.click_menu()
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logout_button)
        ).is_displayed()
    
    def is_login_button_visible(self):
        """Check if the login button is visible in the menu"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_button)
        ).is_displayed()
    
    def is_cart_button_visible(self):
        """Check if the cart button is visible on the home page"""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.cart_button)
        ).is_displayed()
