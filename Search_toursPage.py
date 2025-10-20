import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search_toursPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Ввод данных поиска тура")
    def search_tour(self):
        # Тестовые данные ввода по полям:
        # Откуда = 'Москва'
        # Куда = 'Турция'
        # Дата_вылета = '10 ноября'
        # Длительность = '10 ночей'
        # Кто_едет = "2 взрослых" без детей (по умолчанию)

        # Переход на главную страницу подбора туров
        # Нажать на вкладку "Туры"
        tours_tab = (WebDriverWait(self.__driver, 10).
                     until(EC.element_to_be_clickable((
                          By.XPATH, '//*[@id="app"]/header/'
                          'div/div[2]/div[1]/a'))))
        tours_tab.click()
        # Ожидание загрузки главной страницы поска туров
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.XPATH, '//*[@id="app"]'))))
        print('Главная страница по поиску туров открыта')

        (WebDriverWait(self.__driver, 15).
         until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
            'div[1]/div/div/div[1]/div/div/input')))).click()
        (self.__driver.find_element(
           By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[1]/div[1]/'
           'div/div[1]/div/div[2]/div/div[1]').click())
        print('Город поля "Откуда" введён')

        (self.__driver.find_element(
           By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[1]/div[1]/'
           'div/div[2]/div/div[2]/div/div[3]/div[1]').click())
        print('Страна отдыха поля "Куда" введена')

        # Выбор в поле "Дата вылета" из календаря даты вылета
        number_data = (WebDriverWait(self.__driver, 12).
                       until(EC.element_to_be_clickable((
                          By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
                          'div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/'
                          'div[2]/div[2]/div[15]/div'))))
        number_data.click()
        # второй клик по элементу
        number_data1 = (WebDriverWait(self.__driver, 12).
                        until(EC.element_to_be_clickable((
                           By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
                           'div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/'
                           'div[2]/div[2]/div[15]/div'))))
        number_data1.click()
        print('Дата вылета "10 ноября" введена')

        # Выбор возможного (из активных кнопок) количества ночей
        number_night = (WebDriverWait(self.__driver, 17).
                        until(EC.element_to_be_clickable((
                            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
                            'div[1]/div/div/div[4]/div/div[2]/div[2]/'
                            'div[1]/div[10]'))))
        number_night.click()
        # Второй клик по элементу
        number_night1 = (WebDriverWait(self.__driver, 17).
                         until(EC.element_to_be_clickable((
                            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
                            'div[1]/div/div/div[4]/div/div[2]/'
                            'div[2]/div[1]/div[10]'))))
        number_night1.click()
        print('Длителность отдыха ("Количество ночей = 10") введено')
        # По умолчанию количество отдыхающих 2 взрослых (без детей)
        print('Количество отдыхающих ("Кто едет") введено')

        # Нажатие на кнопку "Найти"
        (WebDriverWait(self.__driver, 10).
         until(EC.element_to_be_clickable((
             By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
             'div[1]/div/div/button')))).click()
        print('Кнопка "Найти" нажата')

        # Ожидание загрузки страницы запроса
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((
             By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/'
             'div/div[2]/div[2]/div[3]'))))
        print('Страница подобранного тура открыта')
