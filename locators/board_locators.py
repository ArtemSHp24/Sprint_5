from selenium.webdriver.common.by import By


class RegistrationLocators:
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    REPEAT_PASSWORD_FIELD = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_TEXT = (By.XPATH, "//span[contains(@class,'input_span') and text()='Ошибка']")
    PROFILE_AVATAR = (By.XPATH, "//button[contains(@class,'circleSmall')]")


class LoginLocators:
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    USER_NAME = (By.XPATH, "//h3[contains(@class,'profileText') and contains(text(),'User')]")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']")


class ProfileLocators:
    USER_NAME = (By.XPATH, "//h3[contains(@class,'profileText') and contains(text(),'User')]")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Выйти']")
    MY_ADS_SECTION = (By.XPATH, "//div[contains(@class,'profile_ads')]")


class AdsLocators:
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    AUTH_MODAL_TEXT = (
    By.XPATH,
    "//h1[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]"
)
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.XPATH, "//select[@name='category']")
    CATEGORY_OPTION_BOOKS = (By.XPATH, "//option[contains(text(),'Книги')]")
    CITY_DROPDOWN = (By.XPATH, "//select[@name='city']")
    CITY_OPTION_MOSCOW = (By.XPATH, "//option[contains(text(),'Москва')]")
    CONDITION_NEW = (By.XPATH, "//input[@type='radio' and @value='new']")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    PROFILE_BUTTON = (By.XPATH, "//a[contains(text(),'Профиль')]")
    AD_IN_PROFILE = (By.XPATH, "//h3[contains(text(),'Книга по Python')]")
