import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.board_locators import LoginLocators
from test_data.texts import BoardTexts


class TestLogin:

    def test_user_can_login(self, driver):

        driver.find_element(*LoginLocators.LOGIN_REGISTER_BTN).click()

        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("Archi@mail.ru")
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("archi123")

        driver.find_element(*LoginLocators.LOGIN_BTN).click()

        user_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.USER_NAME)
        ).text

        assert user_name == BoardTexts.USER_NAME, \
            f"Ожидалось имя '{BoardTexts.USER_NAME}', но получено '{user_name}'"


   