# -*- coding: utf-8 -*-                    C:\Users\edart\selenium_course\graduation-work-stepik-autotest-course\test_product_page.py

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

#Тестовый класс
@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "user" + email
        link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)   
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   
        page.open()    
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   
        page.open()    
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_to_basket()
        page.should_be_product_name(product_name)
        page.should_be_product_price(product_price)

# проверяем возможность добавления в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    
    page.open()    
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_basket()
    page.should_be_product_name(product_name)
    page.should_be_product_price(product_price)

# проверяем переход на страницу входа
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  
    page.open()                      
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)          
    login_page.should_be_login_page()

# Проверяем корзину
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_that_basket_is_empty('empty')
     
