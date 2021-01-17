from pages.base_page import BasePage 
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "It is not login link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        f_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        f_email.send_keys(email)
        f_pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        f_pass1.send_keys(password)
        f_pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        f_pass2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        btn.click()

