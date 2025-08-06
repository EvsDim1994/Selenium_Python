from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGGIN_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    PLACE_ADS_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    USER_LOGO = (By.CLASS_NAME, "circleSmall")
    USER_NAME = (By.XPATH, ".//h3[contains(text(), 'User')]")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    APPLY_BUTTON = (By.XPATH, ".//button[text()='Применить']")


class RegistrationFormLocators():
    REGISTRATION_BUTTON = (By.XPATH, ".//h1[text()='Зарегистрироваться']")
    EMAIL = (By.XPATH, ".//input[@name='email']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    SUBMIT_PASSWORD_BUTTON = (By.XPATH, ".//input[@name='submitPassword']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    ERROR = (By.XPATH, ".//span[text()='Ошибка']")

class LoginForm():
    WITHOUT_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    INPUT_EMAIL = (By.XPATH, ".//input[@placeholder='Введите Email']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@placeholder='Пароль']")
    LOGGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    AUTORIZATION_TEXT = (By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

class AdsForm():
    INPUT_NAME_ADS = (By.XPATH, "//input[@placeholder='Название']")
    INPUT_DISCRIPT_ADS = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    INPUT_PRICE = (By.XPATH, "//input[@placeholder='Стоимость']")
    RADIO_BUTTONS = (By.XPATH, ".//div[@class='radioUnput_shell__Wtdwe']/div[@class='radioUnput_inputRegular__FbVbr']")
    DROP_LIST = (By.XPATH, ".//button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    TECH_CATEGORY = (By.XPATH, ".//span[text()='Технологии']")
    CITY = (By.XPATH, ".//span[text()='Новосибирск']")
    PLACE_ADS_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")

class AdsPage(): 
    PROFILE_TEXT = (By.XPATH, ".//h1[text()='Мой профиль']")
    PRICE_TEXT = (By.XPATH, ".//div[@class='price']/h2[@class='h2'] ")
    DESCRIPTION_TEXT = (By.XPATH, ".//div[@class='about']//h2[@class='h2']")
    CITY = (By.XPATH, ".//div[@class='about']//h3[@class='h3']")
    