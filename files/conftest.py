import allure
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        driver.maximize_window()
        yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()