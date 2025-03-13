import pytest
import time  # ✅ Add this for debugging
from Utilities.webdriver_setup import get_driver
from TestLocators.home_page import HomePageLocators
from pages.home_page import HomePage
def testcase_3_logout_is_visble_and_functioning():
    """Test if the logout button is visible and functioning."""
    driver = get_driver()
    try:
        home_page = HomePage(driver)
        home_page.gotosaucedemohomepage()
        home_page.login('standard_user','secret_sauce')
        home_page_locator = HomePageLocators(driver)
        assert home_page_locator.is_logout_button_visible(), "Logout button not visible"

        print("clicking logout...")
        time.sleep(2)  # ✅ Give time for the menu to open
        home_page_locator.click_logout()
        print("logout successful...")

        assert home_page_locator.is_login_button_visible(), "Logout failed"
       
    except Exception as e:
        driver.save_screenshot("screenshots/test_logout_failure.png")  # 📸 Capture Screenshot
        print(f"ERROR: {e}")  # 🛑 Print error in logs
        raise e
    finally:
        driver.quit()
        