import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_validate_username_input(self, setup):
        login_page = LoginPage(setup)
        assert login_page.validate_username_input()

    def test_validate_password_input(self, setup):
        login_page = LoginPage(setup)
        assert login_page.validate_password_input()

    def test_validate_submit_button(self, setup):
        login_page = LoginPage(setup)
        assert login_page.validate_submit_button()

    def test_unsuccessful_login(self, setup):
        login_page = LoginPage(setup)
        login_page.login("wrong@example.com", "wrongpassword")
        assert "Invalid" in login_page.get_error_message()

    def test_successful_login(self, setup):
        login_page = LoginPage(setup)
        login_page.login("satheeshkanna41@gmail.com", "Bakunamatata@123")
       
        assert "Dashboard" in setup.page_source  
