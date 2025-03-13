"""
Write the test scripts for performing the data driven testing
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Import the data and locators
from TestLocators.locators import SauceLocators
from TestData.data import SauceData
from Utilities.excel_functions import ExcelFunctions
from pages.home_page import HomePage

class TestSauceDDTF:

    def testcase_1_and_2_login_excel(self):
        successfulCount = 0
        failedCount = 0
        self.excel_file = SauceData().excel_file
        self.sheet_number = SauceData().sheet_number

        self.excel = ExcelFunctions(self.excel_file, self.sheet_number)
        

        # get the maximum row count inorder to loop properly
        self.rows = self.excel.row_count()

        # use for loop for fetching the datasets
        for row in range(2, self.rows+1):
            username = self.excel.read_data(row, 5)
            password = self.excel.read_data(row, 6)
            print(f"Attempting login with Username: {username} and Password: {password}")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            page = HomePage(self.driver)
            page.gotosaucedemohomepage()
            page.login(username, password)
            self.driver.implicitly_wait(5)
            # Check if 'session-username' is in session storage
            session_username = self.driver.execute_script("return window.sessionStorage.getItem('session-username');")
            if session_username == username:
                successfulCount += 1
            else:
                failedCount += 1
            self.driver.quit()
        assert int(successfulCount) == 4 and int(failedCount) == 1, f"Expected 4-Success , 1- failed , but found {int(successfulCount)}-Success ,  {int(failedCount)}- failed"