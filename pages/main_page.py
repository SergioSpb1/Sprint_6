from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import Locators
from pages.base_page import BasePage
import allure

class MainPageScooters (BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step("Клик вопроса {question_text}")
    def click_question_by_text(self, question_text):
        dynamic_locator = (By.XPATH, f"//*[contains(text(), '{question_text}')]" )
        self.click_element_with_wait(dynamic_locator)

    @allure.step("Получение ответа на вопрос")
    def get_open_answer_text(self):
        open_answer =  self.find_element_with_wait(Locators.ACTUAL_ANSWER)
        return open_answer.text

    @allure.step("Клик верхней кнопки 'Заказать'")
    def click_top_order_button (self):
        self.click_element_with_wait(Locators.MAIN_TOP_ORDER_BUTTON)

    @allure.step("Клик нижней кнопки 'Заказать'")
    def click_bottom_order_button (self):
        self.click_element_with_wait(Locators.MAIN_BOTTOM_ORDER_BUTTON)
    
 
        