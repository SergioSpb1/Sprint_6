from data import Data
from pages.main_page import MainPageScooters
from pages.order_page import OrderPage
import pytest
import allure

class TestLogos:

    @allure.title("Проверка клика по логотипу 'Самокат'")
    @allure.description("Главная->Заказать(страница заказа)->Самокат. После клика возвращаемся на главную страницу") 
    def test_samokat_logo (self, driver):

        main_page = MainPageScooters(driver)
        main_page.open()
        main_page.click_bottom_order_button() 

        order_page = OrderPage(driver)
        order_page.click_samokat_logo()
        
        assert order_page.check_url_is(Data.BASE_URL)

    @allure.title("Проверка клика по логотипу 'Яндекс'")
    @allure.description("Главная->Заказать(страница заказа)->Яндекс. После клика переход на страницу Дзена")
    def test_yandex_logo (self, driver):

        main_page = MainPageScooters(driver)
        main_page.open()
        main_page.click_bottom_order_button() 

        order_page = OrderPage(driver)
        order_page.click_yandex_logo()
        order_page.switch_to_new_window()
                
        assert order_page.check_url_contains(Data.DZEN_URL_PART)