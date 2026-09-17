import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):

    @allure.step("Заполнение имени")
    def fill_name(self, name):
        field = self.find_element_with_wait(Locators.NAME_INPUT)
        field.clear()
        field.send_keys(name)

    @allure.step("Заполнение фамилии") 
    def fill_last_name(self, last_name):
        field = self.find_element_with_wait(Locators.LAST_NAME_INPUT)
        field.clear()
        field.send_keys(last_name)

    @allure.step("Заполнение адреса")
    def fill_address(self, address):
        field = self.find_element_with_wait(Locators.ADDRESS_INPUT)
        field.clear()
        field.send_keys(address)

    @allure.step("Заполнение телефона") 
    def fill_phone(self, phone):
        field = self.find_element_with_wait(Locators.PHONE_INPUT)
        field.clear()
        field.send_keys(phone)

    @allure.step("Выбор станции метро из выпадающего списка")
    def select_metro_by_index(self, index):
        field = self.find_element_with_wait(Locators.METRO_INPUT)
    
        field.click()
        time.sleep(0.5)
        field.send_keys("С") 
    
        items = self.wait.until(EC.presence_of_all_elements_located(Locators.METRO_SUGGESTIONS_LIST))
        items[index].click()
            
    @allure.step("Нажатие кнопки 'Далее'")
    def submit_form_1(self):
        dalee_button = self.find_element_with_wait(Locators.NEXT_BUTTON)
        dalee_button.click()

    
    def fill_form_one(self, user_data):

        self.fill_name(user_data["name"])
        self.fill_last_name(user_data["f_name"])
        self.fill_address(user_data["address"])
        metro_index = user_data.get("metro_index", 0)
        self.select_metro_by_index(metro_index)
        self.fill_phone(user_data["phone"])
        self.submit_form_1()

    def select_date(self, date_str):
        field = self.find_element_with_wait(Locators.DELIVERY_DATE_INPUT)

        field.click()
        time.sleep(0.3)
        field.clear()
        field.send_keys(date_str)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", field)
        self.driver.find_element(By.TAG_NAME, "body").click() 

    def select_rent_period(self, period_text):
        element = self.find_element_with_wait(Locators.RENT_DURATION_INPUT)
        element.click()

        time.sleep(0.5)

        by_type, template_str = Locators.RENT_DURATION_OPTION_TEMPLATE 
        option_locator = (by_type, template_str.format(period_text))

        target_option = self.wait.until(EC.element_to_be_clickable(option_locator)) 
        self.driver.execute_script("arguments[0].click();", target_option)
        
    def select_colour (self, colour_value):

        colour_map = {"чёрный жемчуг": Locators.COLOUR_BLACK, "серая безысходность": Locators.COLOUR_GREY}

        locator = colour_map.get(colour_value.lower())

        checkbox = self.find_element_with_wait(locator)
        checkbox.click()

    def put_comment(self, comment_text):

        comment = self.find_element_with_wait(Locators.COMMENT_INPUT)
        comment.send_keys(comment_text)

    def submit_form_2(self):
            order_button = self.find_element_with_wait(Locators.FINAL_ORDER_BUTTON)
            order_button.click()

    @allure.step("Заполнение деталей заказа")
    def fill_form_two(self, order_details):

        target_date = order_details["delivery_date"]
        self.select_date(target_date)
        time.sleep(0.5) 
        target_period = order_details["rent_period"]
        self.select_rent_period(target_period)
        self.select_colour(order_details["colour"])
        self.put_comment(order_details["comment"])
        self.submit_form_2()

    @allure.step("Подтверждение заказа") 
    def confirm_order(self):
        self.find_element_with_wait(Locators.CONFIRM_ORDER_BUTTON).click()

    @allure.step("Клик логотипа Самокат")            
    def click_samokat_logo (self):
        self.click_element_with_wait(Locators.SAMOKAT_LOGO)

    @allure.step("Клик логотипа Яндекс") 
    def click_yandex_logo (self):
        self.click_element_with_wait(Locators.YANDEX_LOGO)