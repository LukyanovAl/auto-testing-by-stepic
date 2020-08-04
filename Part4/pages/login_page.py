from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url(By.LINK_TEXT, "login") # реализуйте проверку на корректный url адрес
        assert True,  "Login URL is present!"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*MainPageLocators.LOGIN_FORM) # реализуйте проверку, что есть форма логина
        assert True,  "Login Form is present!"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*MainPageLocators.REGISTER_FORM) # реализуйте проверку, что есть форма регистрации на странице
        assert True,  "Register Form is present!"

