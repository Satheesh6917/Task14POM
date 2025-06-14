import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    print("Launching Zen portal...") 
    driver.get("https://v2.zenclass.in/login")
    yield driver
    driver.quit()
