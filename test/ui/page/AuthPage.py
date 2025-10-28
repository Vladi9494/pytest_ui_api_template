import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://fstravel.com/"
        self.__driver = driver
        print('Сайт тур-оператора "FUN&SUN" открыт')
        """
        Конструктор класса AuthPage.
        """

    @allure.step("Закрыть всплывающие окна, закрывающее видимость сайта")
    def close_pop_ups(self):
        """"
        Ожидает загрузки появляющихся окон рекламы и закрывает их,
        а также выводит в консоль информацию о том, что окно рекламы закрыто.
        """
        self.__driver.get(self.__url)

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

        # Закрыть окно с всплывающей рекламой "Будьте в курсе"
        WebDriverWait(self.__driver, 20).until(
            EC.visibility_of_element_located((
             By.XPATH, "//div[@id='popmechanic-form-86751']/div[4]")))
        self.__driver.find_element(
            By.XPATH, "//*[@id='popmechanic-form-86751']/div[4]")
        print('Окно рекламы "Будьте в курсе" закрыто')

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        """
        Осуществляет поиск кнопки авторизации, нажимает её,
        а также выводит в консоль информацию о том,
        что кнопка авторизации найдена и нажата.
        """
        self.__driver.get(self.__url)
        (self.__driver.find_element(
            By.XPATH, '//*[@id="app"]/div/header/div[1]/div/div/'
            'div/div[2]/div/div[2]/div[1]/div/span[1]')).click()
        print("Кнопка авторизации найдена и нажата")

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        """
        Осуществляет поиск и ожидание видимости соответствующих
        полей авторизации, а также ввод в соответствующие поля {email},
        {password}, нажатие кнопки ввода авторизации,
        осуществляет вывод в консоль информации о том,
        что страница авторизации отобразилась и
        данные авторизации (Email и пароль) введены и то, что
        иконка авторизации на странице сайта поменяла свой вид.
        :param: driver: int - время задержки в секундах
        """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.CSS_SELECTOR, "#email"))))
        (self.__driver.find_element(By.CSS_SELECTOR, "#email").
         send_keys(email))
        print("Страница авторизации отобразилась и Email введён")

        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.CSS_SELECTOR, "#password"))))
        (self.__driver.find_element(By.CSS_SELECTOR, "#password").
         send_keys(password))
        print("Пароль введен")

        (self.__driver.find_element(By.CSS_SELECTOR, "input[type=submit]").
         click())
        print("Кнопка авторизации нажата")

        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.XPATH, '//*[@id="app"]/div/header/div[1]/div/div/'
             'div/div[2]/div/div[2]/div[1]/div/div/div[1]/img'))))
        print("На главной странице сайта "
              "иконка авторизации поменяла свой вид")
