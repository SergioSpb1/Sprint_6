from data import FaqData
from pages.main_page import MainPageScooters
import pytest
import allure

class TestMain:

    @allure.title("Проверка выпадающего списка 'Вопросы о Важном'")
    @allure.description("Параметризованный тест, проверка 8 реальных ответов на соответствие эталонным")
    @pytest.mark.parametrize("test_case", FaqData.QUESTIONS)
    def test_faq_questions(self, driver, test_case):

        main_page = MainPageScooters(driver)
        main_page.open()
        q_text = test_case["question_text"] 
        expected_answer = test_case["answer_text"]
        main_page.click_question_by_text(q_text) 
        actual_answer = main_page.get_open_answer_text()

        assert actual_answer == expected_answer
