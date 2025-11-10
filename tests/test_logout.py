import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.board_locators import LoginLocators


class TestLogout:

    def test_user_can_logout(self, driver):

        driver.find_element(*LoginLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("Archi@mail.ru")
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("archi123")
        driver.find_element(*LoginLocators.LOGIN_BTN).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.USER_NAME)
        )

        driver.find_element(*LoginLocators.LOGOUT_BTN).click()

        login_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.LOGIN_REGISTER_BTN)
        )

        assert login_btn.is_displayed(), "После выхода кнопка 'Вход и регистрация' не появилась."
