import pytest
from selenium import webdriver
from faker import Faker
from locators.board_locators import LoginLocators

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

