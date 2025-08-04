import random
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.locators import MainPageLocators
from src.locators import RegistrationFormLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration():

    def test_succesfull_registration(self, driver: WebDriver, main_page, email, password, teardown):
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON)))
        # Открытие формы регистрации
        driver.find_element(*RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.REGISTRATION)))
        # Ввод данных на регистрационное форме
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(email)
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()
        # Проверки создание аккаунта и переход на главную страницу
        assert driver.find_element(* MainPageLocators.PLACE_ADS).text == "Разместить объявление"
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.USER_LOGO)))
        assert driver.find_element(*MainPageLocators.USER_NAME).text == "User."


    def test_unsuccesfull_registration(self, driver: WebDriver, main_page, password, teardown):
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON)))
        # Открытие формы регистрации
        driver.find_element(*RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.REGISTRATION)))
        # Ввод данных на регистрационное форме с некорректным email
        incorrect_email = random.randint(1000, 9999)
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(str(incorrect_email))
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()
        # Проверки появления текста с ошибкой
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.ERROR)))
        assert driver.find_element(*RegistrationFormLocators.ERROR).text == "Ошибка"


    def test_unsuccesfull_registration_with_the_same_account(self, driver: WebDriver, main_page, email, password, teardown):
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON)))
        # Открытие формы регистрации
        driver.find_element(*RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.REGISTRATION)))
        # Ввод данных на регистрационное форме
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(email)
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()
        # Проверки  переход на главную страницу
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.USER_LOGO)))
        # Нажать на кнопку "Выйти"
        driver.find_element(*MainPageLocators.EXIT).click()
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON)))
        # Открытие формы регистрации
        driver.find_element(*RegistrationFormLocators.WITHOUT_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.REGISTRATION)))
        # Ввод данных на регистрационное форме уже созданного аккаунта
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(email)
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()
        # Проверки появления текста с ошибкой
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((RegistrationFormLocators.ERROR)))
        assert driver.find_element(*RegistrationFormLocators.ERROR).text == "Ошибка"