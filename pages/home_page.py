import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData.data import SauceData
from TestLocators.locators import SauceLocators
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def gotosaucedemohomepage(self):
        self.driver.get(SauceData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def take_screenshot(self, name):
        if not os.path.exists('./reports/screenshots'):
            os.makedirs('./reports/screenshots')
        self.driver.save_screenshot(f'./reports/screenshots/{name}.png')
    
    def click_menu(self):
        menu_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()

    def click_logout(self):
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()

    def is_login_button_visible(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        ).is_displayed()

    def is_logout_button_visible(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        ).is_displayed()

    def is_cart_visible(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
        ).is_displayed()
    
    def is_checkout_completed(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(SauceLocators.CHECKOUT_COMPLETE_CONTAINER)
        ).is_displayed()
    
    def click_finish_button(self):
        finish_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart_button"))
        )
        finish_button.click()
    
    # ✅ Login method
    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    # ✅ Get all product elements
    def get_all_products(self):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

    # ✅ Get cart count
    def get_cart_count(self):
        cart_count_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return cart_count_element.text

    # ✅ Add product to cart
    def add_product_to_cart(self, product):
        add_button = product.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()

    # ✅ Click on cart button
    def click_cart_button(self):
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_button.click()

    # ✅ Get products in cart (name and price)
    def get_cart_products(self):
        product_names = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        products = [(name.text, price.text) for name, price in zip(product_names, product_prices)]
        return products

    # ✅ Click on checkout button
    def click_checkout_button(self):
        checkout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button"))
        )
        checkout_button.click()

    # ✅ Enter checkout details
    def enter_checkout_details(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    # ✅ Click on continue button after entering checkout details
    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart_button"))
        )
        continue_button.click()

    # ✅ Get products at checkout (name and price)
    def get_checkout_products(self):
        product_names = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        products = [(name.text, price.text) for name, price in zip(product_names, product_prices)]
        return products
