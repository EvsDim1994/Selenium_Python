import random
from selenium.webdriver.remote.webdriver import WebDriver
from src.locators import LoginForm, MainPageLocators
from src.locators import RegistrationFormLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistration:

    def test_succesfull_registration(self, driver: WebDriver, main_page, email, password, create_account):
        # Проверки создание аккаунта и переход на главную страницу
        assert driver.find_element(* MainPageLocators.PLACE_ADS_BUTTON).text == "Разместить объявление"
        assert  WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.USER_LOGO))
        assert driver.find_element(*MainPageLocators.USER_NAME).text == "User."


    def test_unsuccesfull_registration(self, driver: WebDriver, main_page, password):
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginForm.WITHOUT_ACCOUNT_BUTTON)).click()
        # Открытие формы регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationFormLocators.REGISTRATION_BUTTON))
        # Ввод данных на регистрационное форме с некорректным email
        incorrect_email = random.randint(1000, 9999)
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(str(incorrect_email))
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD_BUTTON).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()
        # Проверки появления текста с ошибкой
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationFormLocators.ERROR)).text == "Ошибка"


    def test_unsuccesfull_registration_with_the_same_account(self, driver: WebDriver, main_page, email, password, create_account):
        # Проверки  переход на главную страницу
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.USER_LOGO))
        # Нажать на кнопку "Выйти"
        driver.find_element(*MainPageLocators.EXIT_BUTTON).click()
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ожидание появления кнопки "Нет аккаунта"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginForm.WITHOUT_ACCOUNT_BUTTON)).click()
        # Открытие формы регистрации
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationFormLocators.REGISTRATION_BUTTON))
        # Ввод данных на регистрационное форме уже созданного аккаунта
        driver.find_element(*RegistrationFormLocators.EMAIL).send_keys(email)
        driver.find_element(*RegistrationFormLocators.PASSWORD).send_keys(password)
        driver.find_element(*RegistrationFormLocators.SUBMIT_PASSWORD_BUTTON).send_keys(password)
        # Создание аккаунта
        driver.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()
        # Проверки появления текста с ошибкой
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrationFormLocators.ERROR)).text == "Ошибка"
        