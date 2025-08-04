from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGGIN_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    PLACE_ADS = (By.XPATH, ".//button[text()='Разместить объявление']")
    USER_LOGO = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.XPATH, ".//h3[contains(text(), 'User')]")
    EXIT = (By.XPATH, ".//button[text()='Выйти']")


class RegistrationFormLocators():
    WITHOUT_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    REGISTRATION = (By.XPATH, ".//h1[text()='Зарегистрироваться']")
    EMAIL = (By.XPATH, ".//input[@name='email']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    SUBMIT_PASSWORD = (By.XPATH, ".//input[@name='submitPassword']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    ERROR = (By.XPATH, ".//span[text()='Ошибка']")

class LoginForm():
    INPUT_EMAIL = (By.XPATH, ".//input[@placeholder='Введите Email']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@placeholder='Пароль']")
    LOGGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")