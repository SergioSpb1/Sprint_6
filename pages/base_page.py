from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import Locators
import allure

class BasePage:

    TIMER = 0.5

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMER)
        self._close_cookies_if_present()
    
    @allure.step("Поиск и ожидание элемента по локатору") 
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск и ожидание кликабельного элемента по локатору") 
    def find_clickable_element_with_wait(self, locator):  
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Поиск списка элементов по локатору") 
    def find_elements_with_wait(self, locator): 
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик элемента по локатору") 
    def click_element_with_wait(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator)) 
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element) 
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Выполнение JavaScript") 
    def _execute_js(self, script: str, element=None): 
        if element: 
            self.driver.execute_script(script, element) 
        else: self.driver.execute_script(script)

    @allure.step("Клик в тело страницы, чтобы снять фокус")
    def click_page_body(self):
        self.driver.find_element(*Locators.BODY_PAGE).click() 

    @allure.step("Клик по кнопке - закрытие окна про куки") 
    def _close_cookies_if_present(self): 
        try: 
            button = self.wait.until(EC.element_to_be_clickable(Locators.COOK)) 
            button.click() 
        except TimeoutException:
            pass 

    @allure.step("Проверка, что URL содержит строку") 
    def check_url_contains(self, url_part: str, timeout: int = 3): 
        wait = WebDriverWait(self.driver, timeout) 
        return wait.until(EC.url_contains(url_part))

    @allure.step("Проверка, что URL равен равен строке") 
    def check_url_is(self, url: str, timeout: int = 3): 
        wait = WebDriverWait(self.driver, timeout) 
        return wait.until(EC.url_to_be(url))

    @allure.step("Переключение на самую новую вкладку")
    def switch_to_new_window(self, expected_total: int = 2, timeout: int = 5):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(expected_total))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Открытие URL")
    def _go_to(self, url: str):  
        self.driver.get(url)