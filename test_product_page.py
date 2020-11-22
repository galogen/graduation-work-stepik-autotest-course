# -*- coding: utf-8 -*-

from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='error')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()    #открываем страницу
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name(product_name)
    page.should_be_product_price(product_price)
