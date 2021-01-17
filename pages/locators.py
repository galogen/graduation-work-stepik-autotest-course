# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".login_submit")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADDTOBASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")			
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")