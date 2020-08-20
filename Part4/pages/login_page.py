from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url(*MainPageLocators.LOGIN_URL), "Login URL is not corrected"# реализуйте проверку на корректный url адрес
        #assert True,  "Login URL is present!"

    def should_be_login_form(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM), "Login Form doesn't present" # реализуйте проверку, что есть форма логина
        #assert True,  "Login Form is present!"

    def should_be_register_form(self):
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM), "Register Form doesn't present" # реализуйте проверку, что есть форма регистрации на странице
        #assert True,  "Register Form is present!"

