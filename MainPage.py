import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть меню авторизованного пользователя")
    def open_menu(self):
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div/header'
                                   '/div[1]/div/div/div/div[2]'
                                   '/div/div[2]/div[1]/div/div'
                                   '/div[1]/img').click()
        self.__driver.find_element(By.XPATH, '//*[@id="app"]/div/header'
                                   '/div[1]/div/div/div/div[2]/div'
                                   '/div[2]/div[1]/div/div'
                                   '/div[2]/a[1]').click()

    @allure.step("Прочитать информацию о пользователе")
    def get_account_info(self) -> list[str]:
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.XPATH,
                                                 '//*[@id="app"]'
                                                 '/div/div[1]/div'
                                                 '/a/div/div[1]'))))

        # F_n_L_n (First name Last name или Ф.И.О.)
        F_n_L_n = self.__driver.find_element(By.XPATH,
                                             '//*[@id="app"]'
                                             '/div/div[1]/div/a/'
                                             'div/div[1]/div[2]/h4')
        field_email = self.__driver.find_element(By.XPATH, '//*[@id="app"]'
                                                 '/div/div[1]/div/a/div'
                                                 '/div[1]/div[2]/p')

        name = F_n_L_n.text
        email = field_email.text
        return [name, email]
