import random
import pytest
from pages.home_page import HomePage
from TestLocators.locators import SauceLocators
from TestData.data import SauceData
from Utilities.excel_functions import ExcelFunctions
from Utilities.webdriver_setup import get_driver

@pytest.fixture(scope="function")
def setup():
    """Setup and teardown for each test case."""
    driver = get_driver()
    home_page = HomePage(driver)
    home_page.gotosaucedemohomepage()
    home_page.login(SauceData.STANDARD_USER, SauceData.PASSWORD)
    yield driver, home_page
    driver.quit()

# ✅ Test Case 4: Test if the cart button is visible
def testcase_4_is_cart_button_visible(setup):
    """Test if the cart button is visible."""
    driver, home_page = setup
    assert home_page.is_cart_visible(), "Cart button not visible"

# ✅ Test Case 5: Fetch 4 Random Products and Get Names & Prices
def testcase_5_fetch_random_products(setup):
    driver, home_page = setup
    
    # Get all product elements
    products = home_page.get_all_products()
    print(f"products: {len(products)}")
    
    # Select 4 random products
    selected_products = random.sample(products, 4)
    
    fetched_products = []
    for product in selected_products:
        name = product.find_element(*SauceLocators.PRODUCT_NAME).text
        price = product.find_element(*SauceLocators.PRODUCT_PRICE).text
        fetched_products.append((name, price))
    print(f"fetched_products: {len(fetched_products)}")
    # Log and assert
    for name, price in fetched_products:
        print(f"Product: {name}, Price: {price}")
    
    assert len(fetched_products) == 4, "Failed to fetch 4 random products"

# ✅ Test Case 6: Add to Cart and Verify
def testcase_6_add_to_cart(setup):
    driver, home_page = setup
    
    # Get all product elements
    products = home_page.get_all_products()
    selected_products = random.sample(products, 4)
    print(f"selected_products: {len(selected_products)}")
    # Add to cart
    for product in selected_products:
        product.find_element(*SauceLocators.ADD_TO_CART_BUTTON).click()
    
    # Verify cart count
    cart_count = home_page.get_cart_count()
    print(f"selected_products: {len(selected_products)}, cart_count: {int(cart_count)}")
    assert int(cart_count) == 4, f"Expected 4 products, but found {cart_count}"

# ✅ Test Case 7: Verify Products in Cart
def testcase_7_verify_cart_products(setup):
    driver, home_page = setup
    
    # Get all product elements
    products = home_page.get_all_products()
    selected_products = random.sample(products, 4)
    print(f"selected_products: {len(selected_products)}")
    # Add to cart
    for product in selected_products:
        product.find_element(*SauceLocators.ADD_TO_CART_BUTTON).click()
    
    # Navigate to cart
    home_page.click_cart_button()
    
    # Fetch product names and prices in cart
    cart_products = home_page.get_cart_products()
    print(f"Navigate to cart -> cart_products: {len(cart_products)}")
    for name, price in cart_products:
        print(f"Cart Product: {name}, Price: {price}")
    
    assert len(cart_products) == 4, f"Expected 4 products in cart, but found {len(cart_products)}"

# ✅ Test Case 8: Checkout and Fetch Details
def testcase_8_checkout(setup):
    driver, home_page = setup
    
    # Get all product elements
    products = home_page.get_all_products()
    selected_products = random.sample(products, 4)
    print(f"selected_products: {len(selected_products)}")
    # Add to cart
    for product in selected_products:
        product.find_element(*SauceLocators.ADD_TO_CART_BUTTON).click()
    
    # Navigate to cart
    home_page.click_cart_button()
    # Click checkout and fill details
    home_page.click_checkout_button()
    home_page.enter_checkout_details(SauceData.FIRST_NAME, SauceData.LAST_NAME, SauceData.ZIP_CODE)
    home_page.click_continue_button()
    home_page.take_screenshot("checkout_overview")
    # Fetch product names and prices at checkout
    checkout_products = home_page.get_checkout_products()
    
    for name, price in checkout_products:
        print(f"Checkout Product: {name}, Price: {price}")
    
    assert len(checkout_products) == 4, f"Expected 4 products at checkout, but found {len(checkout_products)}"
    home_page.click_finish_button()
    assert home_page.is_checkout_completed(), "Checkout failed"

