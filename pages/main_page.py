from locators import Locators
from data import Data
from pages.base_page import BasePage
import allure

class MainPageScooters (BasePage):

    @allure.step("Открытие базового URL")
    def open(self): 
        self._go_to(Data.BASE_URL)

    @allure.step("Клик вопроса")
    def click_question_by_text(self, question_text):
        locator = Locators.QUESTION(question_text) 
        self.click_element_with_wait(locator)

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

    
    
 
        