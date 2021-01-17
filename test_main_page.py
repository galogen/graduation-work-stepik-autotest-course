# -*- coding: utf-8 -*-

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

# ѕровер€ем, есть сслыка на страницу входа
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# ѕровер€ем, что можем перейти на страницу регистрации и входа с главной
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)          # выполн€ем метод страницы Ч переходим на страницу логина
    login_page.should_be_login_page()

# ѕровер€ем переход на страницу корзины и проверку что она пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_is_empty()
    basket_page.should_be_message_that_basket_is_empty('empty') 


# »спользуем магию ќќѕ 
@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)          # выполн€ем метод страницы Ч переходим на страницу логина
        login_page.should_be_login_page()
        # реализаци€ теста

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        # реализаци€ теста