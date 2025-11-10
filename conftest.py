import pytest
from selenium import webdriver
from faker import Faker

fake = Faker()

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # можешь убрать для визуального теста
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def new_user():
    email = fake.email()
    password = "Qwerty123!"
    return email, password


@pytest.fixture
def authorized_user(driver):
    driver.find_element("xpath", "//button[text()='Вход и регистрация']").click()
    driver.find_element("name", "email").send_keys("existing_user@example.com")
    driver.find_element("name", "password").send_keys("Qwerty123!")
    driver.find_element("xpath", "//button[text()='Войти']").click()
    return driver


@pytest.fixture
def ad_data():
    return "Учебник по Python", "Почти новый, отличное состояние", "1500"
