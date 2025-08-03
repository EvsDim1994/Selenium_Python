from tkinter import Y
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope='function')
def driver():
    # инициализация драйвера
    driver = webdriver.Chrome()
    yield
    # закрытие драйвера
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver: WebDriver):
    # открываем главную страницу
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver