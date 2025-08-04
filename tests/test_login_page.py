from selenium.webdriver.remote.webdriver import WebDriver
from src.locators import MainPageLocators
from src.locators import LoginForm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin():

    def test_succesfull_login(self, driver: WebDriver, main_page, email, password, create_account, teardown):
        # Проверки  переход на главную страницу
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.USER_LOGO)))
        # Нажать на кнопку "Выйти"
        driver.find_element(*MainPageLocators.EXIT).click()
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ввод логина и пароля созданного аккаунта
        driver.find_element(*LoginForm.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginForm.INPUT_PASSWORD).send_keys(password)
        # Нажать на кнопку "Войти"
        driver.find_element(*LoginForm.LOGGIN_BUTTON).click()
        # Проверка входа в аккаунт
        assert  WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.USER_LOGO)))
        assert driver.find_element(*MainPageLocators.USER_NAME).text == "User."

    def test_succesfull_logout(self, driver: WebDriver, main_page, email, password, create_account, teardown):
        # Проверки  переход на главную страницу
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.USER_LOGO)))
        # Нажать на кнопку "Выйти"
        driver.find_element(*MainPageLocators.EXIT).click()
        # Нажать на кнопку "Вход и регистрация"
        driver.find_element(*MainPageLocators.LOGGIN_BUTTON).click()
        # Ввод логина и пароля созданного аккаунта
        driver.find_element(*LoginForm.INPUT_EMAIL).send_keys(email)
        driver.find_element(*LoginForm.INPUT_PASSWORD).send_keys(password)
        # Нажать на кнопку "Войти"
        driver.find_element(*LoginForm.LOGGIN_BUTTON).click()
        # Нажать на кпопку "Выйти"
        driver.find_element(*MainPageLocators.EXIT).click()
         # Проверка выхода из аккаунта
        assert WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located((MainPageLocators.USER_LOGO)))
        assert WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located((MainPageLocators.USER_NAME)))
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.LOGGIN_BUTTON)))
