from pages.base_page import BasePage 
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_login_page(self):
        product_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        product_link.click()

    def go_to_basket_page(self):
        basket_page = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_page.click()

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADDTOBASKET)
        button.click()

    def get_product_name(self):
        pname = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return pname.text

    def get_product_price(self):
        pprice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return pprice.text

    def get_mess_product_name(self):
        pname = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        return pname.text

    def get_mess_product_price(self):
        pprice = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE)
        return pprice.text

    def should_be_product_name(self, prod_name):
        assert prod_name == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text, "Error"

    def should_be_product_price(self, prod_price):
        assert prod_price == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text, "Error"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be disappeared"