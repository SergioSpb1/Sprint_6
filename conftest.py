import pytest 
from selenium import webdriver 

@pytest.fixture(scope="function") 

def driver(): 
    # Инициализация драйвера 
    driver = webdriver.Firefox() 
    driver.maximize_window() 
    yield driver 
    driver.quit()