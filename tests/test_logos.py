from data import Data
from locators import Locators
from pages.main_page import MainPageScooters
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure

class TestLogos:

    @allure.title("Проверка клика по логотипу 'Самокат'")
    @allure.description("Главная->Заказать(страница заказа)->Самокат. После клика возвращаемся на главную страницу")
    
    def test_samokat_logo (self, driver):

        main_page = MainPageScooters(driver)
        driver.get(Data.BASE_URL)
        main_page.click_bottom_order_button() 

        order_page = OrderPage(driver)
        order_page.click_samokat_logo()
        
        assert driver.current_url == Data.BASE_URL

    @allure.title("Проверка клика по логотипу 'Яндекс'")
    @allure.description("Главная->Заказать(страница заказа)->Яндекс. После клика переход на страницу Дзена")
    def test_yandex_logo (self, driver):

        main_page = MainPageScooters(driver)
        driver.get(Data.BASE_URL)
        main_page.click_bottom_order_button() 

        order_page = OrderPage(driver)
        order_page.click_yandex_logo()
               
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
                
        assert WebDriverWait(driver, 3).until(EC.url_contains(Data.DZEN_URL_PART))