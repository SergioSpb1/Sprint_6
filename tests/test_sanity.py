import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure


def test_yandex_title():
    with allure.step("Инициализация драйвера Firefox"):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    
    try:
        with allure.step("Открываем главную страницу Яндекса"):
            driver.get("https://ya.ru")
        
        with allure.step("Проверяем наличие слова 'Яндекс' в заголовке"):
            assert "Яндекс" in driver.title
            
        with allure.step("Делаем скриншот для отчета"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="yandex_main",
                attachment_type=allure.attachment_type.PNG
            )
    finally:
        driver.quit()