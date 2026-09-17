from data import Data, OrderData
from locators import Locators
from pages.main_page import MainPageScooters
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure


class TestOrder:

    @allure.title("Проверка позитивных e2e-сценариев заказа на двух наборах данных")
    @allure.description ("Главная->Заказать->Заполнение формы 1->Заполнение формы 2 -> Подтверждение. После подтверждения появляется окно с текстом 'Заказ оформлен'")
    @pytest.mark.parametrize("test_context", OrderData.ORDERS)
    def test_order_e2e(self, driver, test_context):

        main_page = MainPageScooters(driver)
        driver.get(Data.BASE_URL)

        if test_context["entry_point"] == "top": 
            main_page.click_top_order_button()
        else: 
            main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.fill_form_one(test_context)
        order_page.fill_form_two(test_context)
        order_page.confirm_order()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_CONFIRMATION_HEADER))
   
  
        
