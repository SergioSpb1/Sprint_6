from selenium.webdriver.common.by import By

class Locators:
    #Локаторы главной страницы
    QUESTION = lambda text: (By.XPATH, f"//*[contains(text(), '{text}')]")
    ACTUAL_ANSWER = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel' and not(@hidden)]/p")
    COOK = (By.ID, "rcc-confirm-button")
    MAIN_TOP_ORDER_BUTTON = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    MAIN_BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")

    #Локаторы страницы заказа самоката, экран 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") 
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']") 
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") 
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") 
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']" )    # Пункты выпадающего списка метро (когда кликнем в поле выше) 
    METRO_SUGGESTIONS_LIST = (By.XPATH, "//input[@placeholder='* Станция метро']/ancestor::div[contains(@class, 'select-search')]//following-sibling::div[.//text()]" )
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    BODY_PAGE = (By.TAG_NAME, "body")

    #Локаторы страницы заказа самоката, экран 2
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'привезти самокат')]")
    RENT_DURATION_INPUT = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_DURATION_OPTION_TEMPLATE = ( By.XPATH, "//div[contains(@class, 'Dropdown-option') and normalize-space(text())='{}']" )
    COLOUR_BLACK = (By.ID, "black") 
    COLOUR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[(@placeholder='Комментарий для курьера')]")
    FINAL_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    #Локатор страницы заказа самоката, окно запроса подтверждения
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    #Локаторы страницы заказа самоката, текст "Заказ оформлен" в конкретном окне успешного создания заказа
    ORDER_CONFIRMATION_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and .//text()='Заказ оформлен']")

    #Локаторы логотипов
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")  