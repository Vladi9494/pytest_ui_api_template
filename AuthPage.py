import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://fstravel.com/"
        self.__driver = driver
        print('Сайт "FUN&SUN" открыт')

    # ПОМОГИТЕ ПОЖАЛУЙСТА!!! (сдвинуться с мёртвой точки)
    # НЕ ПОЛУЧАЕТСЯ ЗАКРЫТЬ НАЕЗЖАЮЩЕЕ ОКНО "Испытайте Вашу удачу!"
    # Ругается, что не хватает времени или перехвачен щелчок
    # последующей кнопкой (ставил ожидание от 5 до 200 секунд не помогает),
    # скроллинг не какого эффекта не дал,
    # другие рабочие локаторы не получается найти.

    # локаторы By.CSS_SELECTOR:
    # "[class='close']"
    # "[type='button']"
    # "[data-fl-close.title='Закрыть']"
    # "[title='Закрыть']"

    #  локаторы By.XPATH:
    # "//div[@class='widget js-widget animation_slideLTR']/button[0]"
    # "//*[@id='fl-1002927']/html/body/div/button"
    # "/html/body/div/button"

    @allure.step("Закрыть всплывающие окна, закрывающие видимость сайта")
    def close_pop_ups(self):
        self.__driver.get(self.__url)
        # Закрыть окно с наезжающей рекламой "Испытайте Вашу удачу!"
        try:
            button = WebDriverWait(self.__driver, 30).until(
                EC.element_to_be_clickable((
                   By.XPATH, "//*[@id='fl-1002927']"
                   "/html/body/div/button[0]")))
            self.__driver.execute_script("arguments[0].click();", button)
            # button.click()
        except TimeoutException:
            print("Кнопка не кликабельна "
                  "в течение указанного времени ожидания")

        # Если в ручную закрыть данное ↑окно↑,
        # то дальше ↓↓↓ скрипт работает стабильно

        # Зарыть окно с всплывающей рекламой "Будьте в курсе"
        WebDriverWait(self.__driver, 20).until(
            EC.visibility_of_element_located((
             By.XPATH, "//div[@id='popmechanic-form-86751']/div[4]")))
        self.__driver.find_element(
            By.XPATH, "//*[@id='popmechanic-form-86751']/div[4]")
        # print('окно "Будьте в курсе" закрыто')

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)
        (self.__driver.find_element(
            By.XPATH, '//*[@id="app"]/div/header/div[1]/div/div/'
            'div/div[2]/div/div[2]/div[1]/div/span[1]')).click()
        # print("Кнопка авторизации найдена и нажата")

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):

        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.CSS_SELECTOR, "#email"))))
        (self.__driver.find_element(By.CSS_SELECTOR, "#email").
         send_keys(email))
        # print("Страница авторизации отобразилась и Email введён")

        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.CSS_SELECTOR, "#password"))))
        (self.__driver.find_element(By.CSS_SELECTOR, "#password").
         send_keys(password))
        # print("Пароль введен")

        (self.__driver.find_element(By.CSS_SELECTOR, "input[type=submit]").
         click())
        # print("Кнопка авторизации нажата")

        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.XPATH, '//*[@id="app"]/div/header/div[1]/div/div/'
             'div/div[2]/div/div[2]/div[1]/div/div/div[1]/img'))))
        # print("На главной странице сайта
        # иконка авторизации поменяла свой вид")
