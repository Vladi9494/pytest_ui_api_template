import allure
import pytest
from selenium import webdriver
from page.AuthPage import AuthPage
from page.MainPage import MainPage
from page.Search_4toursPage import Search_4toursPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации, открытия сайта туроператора "FUN&SUN"
    и завершения работы драйвера.
    """
    # Открыть сайт "FUN&SUN"
    driver = webdriver.Chrome()
    # driver.implicitly_wait(6)
    driver.maximize_window()
    driver.get("https://fstravel.com/")
    yield driver
    driver.quit()


@allure.title("Тестирование сайта 'FUN&SUN' по подбору туров")
@allure.description("Тест проверяет корректность работы сайта Fun&SUN"
                    "по поиску и просмотру туров с различными операциями"
                    "по подбору туров отдыха.")
@allure.feature("Сайт туроператора 'FUN&SUN'")
@allure.severity(allure.severity_level.CRITICAL)
def test_auth(driver):

    auth_page = AuthPage(driver)
    with allure.step("Закрыть всплывающие окна, закрывающие видимость сайта"):
        auth_page.close_pop_ups()

    with allure.step("Перейти на страницу авторизации"):
        auth_page.go()

    with allure.step("Ввод данных для авторизации 'email''password'"
                     " и нажатие кнопки авторизации"):
        auth_page.login_as("v67870995@gmail.com", "Максим")

    main_page = MainPage(driver)
    with allure.step("Открыть меню авторизованного пользователя"):
        main_page.open_menu()

    with allure.step(
        "Прочитать информацию о пользователе"
         "'expected_name''expected_email'"):
        main_page.get_account_info(
            "Максимов Владимир Станиславович", "v67870995@gmail.com")
        search_tours_page = Search_4toursPage(driver)
    with allure.step("Ввод данных поиска тура"):
        search_tours_page.search_tour()

    with allure.step("Ввод данных поиска поля 'Откуда'"):
        search_tours_page.input_departure_city()

    with allure.step("Ввод данных поиска поля 'Куда'"):
        search_tours_page.input_arrival_country()

    with allure.step("Ввод данных поиска поля 'Дата вылета'"):
        search_tours_page.input_data_departure()

    with allure.step("Ввод данных поиска поля 'Колиество ночей'"):
        search_tours_page.input_number_night()

    with allure.step("Ввод данных поиска поля 'Кто едет'"):
        search_tours_page.input_number_person()

    with allure.step("Нажатие кнопки 'Найти'"):
        search_tours_page.push_search()
