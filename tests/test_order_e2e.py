from data import OrderData
from locators import Locators
from pages.main_page import MainPageScooters
from pages.order_page import OrderPage
import pytest
import allure


class TestOrder:

    @allure.title("Проверка позитивных e2e-сценариев заказа на двух наборах данных")
    @allure.description ("Главная->Заказать->Заполнение формы 1->Заполнение формы 2 -> Подтверждение. После подтверждения появляется окно с текстом 'Заказ оформлен'")
    @pytest.mark.parametrize("test_context", OrderData.ORDERS)
    def test_order_e2e(self, driver, test_context):

        main_page = MainPageScooters(driver)
        main_page.open()

        #Формируем имя нужного метода клика кнопки (верхней или нижней) вместо условий, согласно замечанию ревьювера
        method_name = f"click_{test_context['entry_point']}_order_button"
        getattr(main_page, method_name)()

        order_page = OrderPage(driver)
        order_page.fill_form_one(test_context)
        order_page.fill_form_two(test_context)
        order_page.confirm_order()

        confirmation_header = order_page.find_element_with_wait(Locators.ORDER_CONFIRMATION_HEADER)
        assert confirmation_header.is_displayed() 
   
  
        
