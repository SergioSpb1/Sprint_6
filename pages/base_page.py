from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import Locators

class BasePage:

    TIMER = 2

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMER)
        self._close_cookies_if_present()
    

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element_with_wait(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator)) 
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element) 
        self.driver.execute_script("arguments[0].click();", element)

    def _close_cookies_if_present(self): 
        try: 
            button = self.wait.until(EC.element_to_be_clickable(Locators.COOK)) 
            button.click() 
        except TimeoutException:
            pass 