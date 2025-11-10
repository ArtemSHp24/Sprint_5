import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.board_locators import AdsLocators, LoginLocators
from test_data.ads_data import AD_TITLE, AD_DESCRIPTION, AD_PRICE
from selenium.webdriver.common.by import By


class TestAds:

    def test_create_ad_unauthorized_user(self, driver):

        driver.find_element(*AdsLocators.CREATE_AD_BUTTON).click()

        modal_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdsLocators.AUTH_MODAL_TEXT)
        ).text.strip()

        assert "Чтобы разместить объявление" in modal_text, \
            f"Не найден ожидаемый текст, найдено: {modal_text}"

    def test_create_ad_authorized_user(self, driver):

        # Авторизация
        driver.find_element(*LoginLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys("rich@mail.ru")
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys("rich123")
        driver.find_element(*LoginLocators.LOGIN_BTN).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.USER_NAME)
        )

        # Создание объявления
        driver.find_element(*AdsLocators.CREATE_AD_BUTTON).click()
        driver.find_element(*AdsLocators.TITLE_INPUT).send_keys(AD_TITLE)

        description_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdsLocators.DESCRIPTION_INPUT)
        )
        driver.execute_script("arguments[0].scrollIntoView();", description_field)
        description_field.send_keys(AD_DESCRIPTION)

        driver.find_element(*AdsLocators.PRICE_INPUT).send_keys(AD_PRICE)

        publish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdsLocators.PUBLISH_BUTTON)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", publish_button)
        publish_button.click()

        WebDriverWait(driver, 5).until(
        EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/")
    )

        # --- Новый блок: проверка объявления после публикации ---

        # Клик по аватарке пользователя, чтобы открыть профиль
        user_avatar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdsLocators.PROFILE_AVATAR)
        )
        user_avatar.click()

        # Скроллим вниз до блока с объявлениями
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        ad_last = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='card'])[last()]"))
        )
        assert ad_last.is_displayed(), "Последнее объявление не отобразилось в профиле."