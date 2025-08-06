import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from src.locators import LoginForm, MainPageLocators, AdsForm, AdsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestCreateAds:

    def test_unsuccesfull_create_ads(self, driver: WebDriver, main_page):
        # Нажать на кнопку "Разместить объявление"
        driver.find_element(*MainPageLocators.PLACE_ADS_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginForm.AUTORIZATION_TEXT))
        assert driver.find_element(*LoginForm.AUTORIZATION_TEXT).text == "Чтобы разместить объявление, авторизуйтесь"


    def test_succesfull_create_ads(self, driver: WebDriver, main_page, create_account):
        # Проверка перехода на главную страницу
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.USER_LOGO))
        # Нажать на кнопку "Разместить объявление"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PLACE_ADS_BUTTON)).click()
        # Ввод данных для создания объявления
        driver.find_element(*AdsForm.INPUT_DISCRIPT_ADS).send_keys("Тест")
        driver.find_element(*AdsForm.INPUT_NAME_ADS).send_keys("Товар")
        driver.find_element(*AdsForm.INPUT_PRICE).send_keys(str(1000))
        # Выбор категории объявления
        driver.find_elements(*AdsForm.DROP_LIST)[0].click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AdsForm.TECH_CATEGORY))
        driver.find_element(*AdsForm.TECH_CATEGORY).click()
        # Выбор города
        driver.find_elements(*AdsForm.DROP_LIST)[1].click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AdsForm.CITY))
        driver.find_element(*AdsForm.CITY).click()
        # Выбор состояния товара
        driver.find_elements(*AdsForm.RADIO_BUTTONS)[0].click()
        # Нажатие на кнопку "Опубликовать"
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(AdsForm.PLACE_ADS_BUTTON)).click()
        # Переход в личный кабинет пользователя
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.APPLY_BUTTON))
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.USER_LOGO)).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AdsPage.PROFILE_TEXT))
        # Проверка создания объявления
        assert driver.find_element(*AdsPage.DESCRIPTION_TEXT).text == "Товар"
        assert driver.find_element(*AdsPage.CITY).text == "Новосибирск"
        assert driver.find_element(*AdsPage.PRICE_TEXT).text == "1 000 ₽"
