"""
This File contains all the locators
"""
from selenium.webdriver.common.by import By

class SauceLocators:
        MENU_BUTTON = (By.CLASS_NAME, "bm-burger-button")
        LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
        LOGIN_BUTTON = (By.ID, "login-button")
        CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
        PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
        PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
        ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
        CHECKOUT_COMPLETE_CONTAINER = (By.CLASS_NAME, "checkout_complete_container")
        username_locator = 'user-name' 
        password_locator = 'password'
        loginbutton_locator = 'login-button'