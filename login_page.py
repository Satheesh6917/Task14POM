from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@placeholder='Enter your mail']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    Signin_BTN = (By.XPATH, "//button[contains(text(),'Sign in')]")
    # ERROR_MSG = (By.XPATH, "//div[contains(text(),'Invalid')]")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.Signin_BTN)

    def validate_username_input(self):
        return self.is_element_visible(self.USERNAME)

    def validate_password_input(self):
        return self.is_element_visible(self.PASSWORD)

    def validate_submit_button(self):
        return self.is_element_visible(self.Signin_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)
