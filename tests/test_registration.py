import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.board_locators import RegistrationLocators
from test_data.texts import BoardTexts


class TestRegistration:

    def test_register_new_user(self, driver, new_user):
        email, password = new_user

        driver.find_element(*RegistrationLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BTN).click()

        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys(password)

        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BTN).click()

        user_avatar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.PROFILE_AVATAR)
        )
        assert user_avatar.is_displayed(), "Аватар пользователя не отобразился после регистрации"


    def test_register_invalid_email(self, driver):
        driver.find_element(*RegistrationLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BTN).click()

        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys("invalidemail")
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("Qwerty123!")
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys("Qwerty123!")
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BTN).click()

        error_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.ERROR_TEXT)
        ).text

        assert error_text == BoardTexts.REGISTRATION_ERROR, \
            f"Ожидалось сообщение '{BoardTexts.REGISTRATION_ERROR}', но получено '{error_text}'"


    def test_register_existing_user(self, driver):
        driver.find_element(*RegistrationLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BTN).click()

        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys("existing_user@example.com")
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("Qwerty123!")
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys("Qwerty123!")
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BTN).click()

        error_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.ERROR_TEXT)
        ).text

        assert error_text == BoardTexts.REGISTRATION_ERROR, \
            f"Ожидалось сообщение '{BoardTexts.REGISTRATION_ERROR}', но получено '{error_text}'"
