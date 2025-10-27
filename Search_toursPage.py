import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException


class Search_toursPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://fstravel.com/searchtour/"

        self.__driver = driver
        print('Сайт тур-оператора "FUN&SUN"'
              'авторизованного пользователя открыт')

        # ЕСЛИ ПОЯВЛЯЕТСЯ КАПЧА то в ручную пройти капчу по ссылке:
        # https://fstravel.com/xpvnsulc/?back_location=https%3A%2F%2F
        # fstravel.com%2Fsearchtour&hcheck=0094083e4b14bc7d39afdde8ace
        # 7d415&request_datetime=2025-10-25+11%3A44%3A30+%2B0000&
        # request_ip=185.90.100.186&request_id=UijwWo2lZ0U1&srv=04038a
        # 63ede07951becb6acafa6bf6fc&copts_k=93ab62af3bb131aeaad6f05c0
        # 8b15bfebc286cd1f3b2f5ddf2afdf23ee27ab681a9f8e02340b492c0d639
        # 4a79dd9c589afdd79314b709613041105b96830b601&oirutpspid=17613
        # 92533363_47d4f4ec73d35f56c6c78ea8a364cb1f_iexew8ni5gokcxi0
        # &oirutpspsc=1761392670250_e5fe18c52f7ff5a9fc1d52d1d2c81cff_q
        # nq-rQ7ZadwPMgWi6-rp2zWS2wobOE8XTcuITv6.KmAZ&oirutpspjs=17613
        # 92670250_267907fc_01350190_c1a54437

    def close_pop_up(self):
        """
        Ожидает появления всплывающего окна рекламы и закрывает его,
        выводит информацию о закрытии или об ошибках.
        """
        self.__driver.get(self.__url)
        try:
            # Ожидание кнопки закрытия до 30 секунд
            button = WebDriverWait(self.__driver, 35).until(
                EC.element_to_be_clickable((
                    By.XPATH, "//button[contains(text(), 'Закрыть')]"))
            )
            # Кликаем через js, чтобы обойти возможные наложения
            self.__driver.execute_script("arguments[0].click();", button)

            print("Окно рекламы 'Испытайте Вашу удачу!' закрыто.")
        except TimeoutException:
            print("Время ожидания истекло: кнопка закрытия окна рекламы "
                  " не появилась или не кликабельна.")
        except NoSuchElementException:
            print("Кнопка закрытия окна рекламы не найдена.")
        except ElementClickInterceptedException:
            print("Кнопка закрытия перекрыта другим элементом,"
                  " клик невозможен.")

    @allure.step("Ввод данных поиска тура")
    def search_tour(self):
        """
        Осуществляет ожидание кликабельности и нажатие
        на вкладку 'Туры', переходит и ожидает загрузки
        главной страницы по поиску и подбору туров,
        а также выводит в консоль информацию  том,
        что главная страница по подбору туров открыта.
        :param: __driver: int время задержки в секундах
        """
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

        # Тестовые данные ввода по полям:
        # Откуда = 'Санкт-Петербург'
        # Куда = 'Тайланд'
        # Дата_вылета = '10 декабря'
        # Длительность = '10 ночей'
        # Кто_едет = "2 взрослых" без детей (по умолчанию)

    @allure.step("Ввод данных поиска поля'откуда'")
    def input_departure_city(self):
        """
        Ожидает видимости поля 'Откуда' и
        осуществляет поиск и выбор города вылета,
        выводит в консоль информацию о том,
        что город в поле 'Откуда' введён.
        :param: __driver: int время задержки в секундах
        """

        (WebDriverWait(self.__driver, 15).
         until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[1]/'
            'div[1]/div/div[1]')))).click()
        (WebDriverWait(self.__driver, 15).
         until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[1]/'
            'div[1]/div/div[1]/div/div[2]/div/div[2]')))).click()
        print('Город поля "Откуда" введён')

    @allure.step("Ввод данных поиска поля 'Куда'")
    def input_arrival_country(self):
        """
        Осуществляет поиск и выбор страны отдыха,
        а также выводит в консоль информацию о том,
        что страна отдыха в поле 'Куда' введена.
        """
        (WebDriverWait(self.__driver, 15).
         until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[1]/'
            'div[1]/div/div[2]/div/div[2]/div/div[8]')))).click()
        print('Страна отдыха поля "Куда" введена')

    @allure.step("Ввод данных поиска поля 'Дата вылета'")
    def input_data_departure(self):
        """
        Ожидает кликабельности и выбор даты вылета
        из списка календаря предложенных дат вылета,
        выводит в консоль информацию о том,
        что конкретная дата вылета введена.
        :param: __driver: int время задержки в секундах
        """
        number_data = (WebDriverWait(self.__driver, 15).
                       until(EC.element_to_be_clickable((
                          By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
                          'div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/'
                          'div[2]/div[2]/div[10]/div'))))
        number_data.click()
        # второй клик по элементу
        number_data1 = (WebDriverWait(self.__driver, 15).
                        until(EC.element_to_be_clickable((
                           By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/'
                           'div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/'
                           'div[2]/div[2]/div[10]/div'))))
        number_data1.click()
        print('Дата вылета "10 декабря" введена')

    @allure.step("Ввод данных поиска 'Колиество ночей'")
    def input_number_night(self):
        """
        Ожидает кликабельности и выбор возможного
        (из активных кнопок) количества ночей,
        выводит в консоль информацию о том,
        что длительность отдыха конкретного количества
        ночей введена.
        :param: __driver: int время задержки в секундах
        """
        number_night = (WebDriverWait(self.__driver, 17).
                        until(EC.element_to_be_clickable((
                            By.XPATH, '//*[@id="app"]/div/div[1]/div/div/'
                            'div/div[1]/div/div/div[4]/div/div[2]/div[2]/'
                            'div[1]/div[10]'))))
        number_night.click()
        # Второй клик по элементу
        number_night1 = (WebDriverWait(self.__driver, 17).
                         until(EC.element_to_be_clickable((
                            By.XPATH, '//*[@id="app"]/div/div[1]/div/'
                            'div/div/div[1]/div/div/div[4]/div/div[2]/'
                            'div[2]/div[1]/div[10]'))))
        number_night1.click()
        print('Длителность отдыха ("Количество ночей = 10") введено')

    @allure.step("Ввод данных поиска поля 'Кто едет'")
    def input_number_person(self):
        """
        Выводит в консоль информацию о количестве
        отдыхающих в поле 'Кто едет'
        """
        # По умолчанию количество отдыхающих 2 взрослых (без детей)
        print('Количество отдыхающих ("Кто едет") введено')

    @allure.step("Нажатие кнопки 'Найти',"
                 " ожидание отображения страницы запроса поиска тура")
    def push_search(self):
        """
        Ожидает кликабельности, а также нажатие кнопки 'Найти',
        выводит в консоль информацию, что кнопка 'Найти' нажата,
        а также ожидает загрузки и отображения страницы запроса и
        вывод в консоль информации о том,
        что страница подобранного тура открыта.
        :param:  __driver: int время задержки в секундах
        """
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

        # Проверка введённых данных в результате запроса
        input_validation = (WebDriverWait(self.__driver, 10).
                            until(EC.visibility_of_element_located((
                                By.XPATH, '//*[@id="search-hotel-card1"]/div/'
                                'div[2]/div[3]/div[1]/div[1]'))))
        element_text = input_validation.text
        assert element_text == "10 дек. • 2 взрослых • 10 ночей"

