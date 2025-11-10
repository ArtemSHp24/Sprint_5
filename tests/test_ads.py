import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.board_locators import AdsLocators, LoginLocators
from test_data.texts import BoardTexts


class TestAds:

    def test_create_ad_unauthorized_user(self, driver):

        driver.find_element(*AdsLocators.CREATE_AD_BUTTON).click()

        modal_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdsLocators.AUTH_MODAL_TEXT)
        ).text.strip()

        assert "Чтобы разместить объявление" in modal_text, \
            f"Не найден ожидаемый текст, найдено: {modal_text}"

    def test_create_ad_authorized_user(self, driver):

        driver.find_element(*LoginLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("rich@mail.ru")
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("rich123")
        driver.find_element(*LoginLocators.LOGIN_BTN).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.USER_NAME)
        )

        driver.find_element(*AdsLocators.CREATE_AD_BUTTON).click()
        driver.find_element(*AdsLocators.TITLE_INPUT).send_keys("Книга по Python")

        description_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdsLocators.DESCRIPTION_INPUT)
        )
        driver.execute_script("arguments[0].scrollIntoView();", description_field)
        description_field.send_keys("Отличная книга для начинающих программистов.")

        driver.find_element(*AdsLocators.PRICE_INPUT).send_keys("500")

        publish_button = driver.find_element(*AdsLocators.PUBLISH_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView();", publish_button)
        publish_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdsLocators.CREATE_AD_BUTTON)
        )
