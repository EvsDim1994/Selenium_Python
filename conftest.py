import random
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture(scope='function')
def main_page(driver: WebDriver):
    # открываем главную страницу
    driver.get("https://qa-desk.stand.praktikum-services.ru")

@pytest.fixture(scope='function')
def teardown(driver: WebDriver):
    yield
    # закрытие драйвера
    driver.quit()

@pytest.fixture(scope='function')
def email():
    # Генерация email
    random_number = random.randint(1000, 9999)
    return f"test{random_number}@testdomain.com"

@pytest.fixture(scope='function')
def password():
    # Генерация password
    random_number = random.randint(1000, 9999)
    return random_number