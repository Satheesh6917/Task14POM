from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_for_element(by_locator).click()

    def enter_text(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        return self.wait_for_element(by_locator).text

    def is_element_visible(self, by_locator):
        try:
            self.wait_for_element(by_locator)
            return True
        except:
            return False
