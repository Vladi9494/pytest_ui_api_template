import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        """
        Конструктор класса MainPage.
        """

    @allure.step("Открыть меню авторизованного пользователя")
    def open_menu(self):
        """
        Осуществляет поиск и открытие меню авторизованного пользователя.
        """
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div/header'
                                   '/div[1]/div/div/div/div[2]'
                                   '/div/div[2]/div[1]/div/div'
                                   '/div[1]/img').click()
        self.__driver.find_element(By.XPATH, '//*[@id="app"]/div/header'
                                   '/div[1]/div/div/div/div[2]/div'
                                   '/div[2]/div[1]/div/div'
                                   '/div[2]/a[1]').click()

    @allure.step("Закрыть всплывающие окна, закрывающее видимость сайта")
    def close_pop_ups(self):
        """"
        Ожидает загрузки появляющихся окон рекламы и закрывает их,
        а также выводит в консоль информацию о том, что окно рекламы закрыто.
        """
        self.__driver.get(self.__url)
        try:
            # Ожидание кнопки закрытия до 20 секунд
            button = WebDriverWait(self.__driver, 20).until(
                EC.element_to_be_clickable((
                    By.XPATH, "//button[contains(text(), 'Закрыть')]"))
            )
            # Кликаем через js, чтобы обойти возможные наложения
            self.__driver.execute_script("arguments[0].click();", button)

            print("Окно рекламы 'Испытайте Вашу удачу!' закрыто.")
        except TimeoutException:
            print("Время ожидания истекло: кнопка закрытия окна рекламы "
                  "не появилась или не кликабельна.")
        except NoSuchElementException:
            print("Кнопка закрытия окна рекламы не найдена.")
        except ElementClickInterceptedException:
            print("Кнопка закрытия перекрыта другим элементом,"
                  "клик невозможен.")

    @allure.step("Прочитать информацию о пользователе"
                 "{expected_name}:{expected_email}")
    def get_account_info(self, expected_name: str,
                         expected_email: str) -> list[str]:
        """
        Осуществляет поиск и ожидание видимости информации об
        авторизованном пользователе, а также считывание и возвращение
        данной информации (Ф.И.О., email)
        :param: __driver: int время задержки в секундах
        :return: str - текст Ф.И.О., email авторизованного пользователя.
        :param expected_name: ожидаемое Ф.И.О.
        :param expected_email: ожидаемый email
        :return: [name, email]
        """
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

        # Проверка соответствия данных
        assert name == expected_name
        assert email == expected_email

        return [name, email]
