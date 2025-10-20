from page.AuthPage import AuthPage
from page.MainPage import MainPage
from page.Search_toursPage import Search_toursPage


def test_auth(driver):
    # email = test_data.get("email")  - почему-то не работает?
    # password = test_data.get("password")
    # email = "v67870995@gmail.com"
    # password = "Максим"

    auth_page = AuthPage(driver)
    auth_page.close_pop_ups()
    auth_page.go()
    auth_page.login_as("v67870995@gmail.com", "Максим")

    main_page = MainPage(driver)
    main_page.open_menu()

    search_test_page = Search_toursPage(driver)
    search_test_page.search_tour()
