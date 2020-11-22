# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".login_submit")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, ".registration_submit")

class ProductPageLocators():
    BUTTON_ADDTOBASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")			
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_LINK = (By.CSS_SELECTOR, "#login_link")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")