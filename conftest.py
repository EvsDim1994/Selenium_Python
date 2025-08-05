import random
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from src.locators import LoginForm, MainPageLocators
from src.locators import RegistrationFormLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
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

@pytest.fixture(scope='function')
def create_account(driver, email, password):
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((LoginForm.WITHOUT_ACCOUNT_BUTTON)))
        # Открытие формы регистрации
        driver.find_element(*LoginForm.WITHOUT_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.REGISTRATION_BUTTON)))
        # Ввод данных на регистрационное форме
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(email)
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD_BUTTON).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()

