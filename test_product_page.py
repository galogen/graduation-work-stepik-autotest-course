# -*- coding: utf-8 -*-                    C:\Users\edart\selenium_course\graduation-work-stepik-autotest-course\test_product_page.py

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

# ѕровер€ем, что есть возможность перейти на страницу входа
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# ѕровер€ем, что открыта€ страница страница входа
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)          # выполн€ем метод страницы Ч переходим на страницу логина
    login_page.should_be_login_page()

# «адание: независимость контента, ищем баг
#@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='error')) for i in range(10)])
#def test_guest_can_add_product_to_basket(browser, promo_offer):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
#    page.open()    #открываем страницу
#    product_name = page.get_product_name()
#    product_price = page.get_product_price()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.should_be_product_name(product_name)
#    page.should_be_product_price(product_price)

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()    #открываем страницу
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_be_product_name(product_name)
    page.should_be_product_price(product_price)

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)          # выполн€ем метод страницы Ч переходим на страницу логина
    login_page.should_be_login_page()

# Ќегативные проверки
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()    #открываем страницу
    page.add_to_basket()
    page.should_not_be_success_message()

# Ќегативные проверки
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()    #открываем страницу
    page.should_not_be_success_message()

# Ќегативные проверки
@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()    #открываем страницу
    page.add_to_basket()
    page.should_be_success_message_is_disappeared()

# ѕровер€ем корзину
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_that_basket_is_empty('empty') 

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "user" + email
        link = f"http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
        page.open()    #открываем страницу
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
        page.open()    #открываем страницу
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_to_basket()
        page.should_be_product_name(product_name)
        page.should_be_product_price(product_price)
         
