# -*- coding: utf-8 -*-

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_page(self):
        basket_page = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_page.click()
