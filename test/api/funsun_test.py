import requests


BASE_URL = (
   "https://fstravel.com/api/service-api/f-s/search/get-by-country?"
   "&minStartDate=2025-11-10&maxStartDate=2025-11-10&minNightsCount=10"
   "&maxNightsCount=10&adults=2&flightTypes=all&sort=recommendations_FS"
)
DEFAULT_HEADERS = {
    "accept": "application/json",
    "User-Agent": "pytest tester",
}

# 1. Позитивный поиск: указаны реальные departureCityId и arrivalCountryId
#  которые есть в списке вкладок "Откуда" и "Куда"
#  например: из Мурманска в Абхазию


def test_positive_search_tour1():

    url = BASE_URL + "departureCityId=274286&arrivalCountryId=233909"
    response = requests.get(url, headers=DEFAULT_HEADERS)

    assert response.status_code == 200
    assert "233909" in response.text
    # assert "Абхазия" in response.text
    # assert "Абхазия" in response.json
    print(response.text)


# 2. Позитивный поиск: реально существующий arrivalCountryId ("Турция")


def test_positive_search_tour2():
    url = BASE_URL + "departureCityId=274286&arrivalCountryId=18803"
    response = requests.get(url, headers=DEFAULT_HEADERS)
    assert response.status_code == 200
    assert "18803" in response.text
    # assert "Турция" in response.text
    # assert "Турция" in response.json()
    # assert {"filters": {"country": {"localizedName": "Турция"}}}
    print(response.text)

    # 3. Негативный: departureCityId фиктивный, несуществующий
    # которого нет в списке городов вкладки "Откуда"(нет id = 999999)


def test_negative_search_tour1():
    url = BASE_URL + "departureCityId=999999&arrivalCountryId=18803"
    response = requests.get(url, headers=DEFAULT_HEADERS)

    assert response.status_code in [200]
    # assert [] in response.text

    print(response.text)

    # 4. Негативный: не указан departureCityId (пустое поле)


def test_negative_search_tour2():
    url = BASE_URL + "departureCityId=&arrivalCountryId=18803"
    response = requests.get(url, headers=DEFAULT_HEADERS)

    assert response.status_code in [200]
    assert "error" in response.text
    assert "The departureCityId field is required." in response.text
    print(response.text)

    # 5. Негативный: поиск по arrivalCountryId без Cookie


def test_negative_search_tour3():

    url = BASE_URL + "departureCityId=274286&arrivalCountryId=18803"
    headers_no_cookie = DEFAULT_HEADERS.copy()
    headers_no_cookie.pop("Cookie", None)
    response = requests.get(url, headers=headers_no_cookie)

    # assert response.status_code == 500
    assert {"message": "Server Error"} in response.json
    print(response.text)
