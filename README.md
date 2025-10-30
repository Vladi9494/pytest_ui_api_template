# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/Vladi9494/
pytest_ui_api_template.git'   
2. Установить зависимости
3. Запустить тесты 'python -m pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- ./ configuration - провайдер настроек
      - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
      - test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
- pip install pytest-playwright 

# Документация проекта

# pytest_ui_api_template
-config
    - .gitignore
    - conf.ini
    - conftest.py
    - DataProvided.py
    - pytest.ini
    - test_config.ini
    - test_data.json
- page
     - AuthPage.py
     - MainPage.py
     - Search_1toursPage.py
     - Search_2toursPage.py
     - Search_3toursPage.py
     - Search_4toursPage.py
- test
    - api
          - funsun_test.py
    - ui 
          - auth_test.py
          - search_1test.py
          - search_2test.py
          - search_3test.py
          - search_4test.py
- README.md          

## Описание базового синтаксиса записи и форматирования

Проект использует следующие технологии и синтаксис:

1. **Python**: Основной язык программирования для написания тестов.
2. **Selenium**: Библиотека для автоматизации взаимодействия с веб-браузером.
3. **Pytest**: Фреймворк для написания и запуска тестов.
4. **Allure**: Инструмент для генерации отчетов о выполнении тестов.

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Используются docstrings для документирования методов и функций.
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step`
 для улучшения читаемости отчетов.

---
## Инстукция по запуску тестов для отладки (из директории где находятся тесты)

1. Команда для запуска отдельного теста например auth_test.py
```python -m pytest auth_test.py```
2. Команда для запуска всех тестов
```python -m pytest```
## Инструкция по запуску тестов для формирования отчета Allure
 
1. Эта команда запустит все тесты и сохранит результаты в директорию "allure-result"
(появляется папка "allure-result"): 
```python -m pytest --alluredir allure-result```

2. Эта команда для запуска тестов: 
```python -m pytest -s -v ```


## Инструкция по просмотру сформированного отчета Allure

1. Эта команда запустит локальный сервер, конвертирует результат в отчёт
   и откроет отчет в браузере: 
```allure serve allure-result```

2.  эта команда генерирует результат в отчёт (появляется папка "allure-report"):
```allure generate allure-result```

3. Эта команда для генерации отчета: 
```allure gnerate allure files -o allure-report```

4. С помощью этой команды можно просмотреть отчёт: 
```allure open allure-report```

 В отчете Allure вы увидите:
   - **Название теста**: `Тестирование сайта туроператора FUN&SUN`.
   - **Описание теста**: Тест проверяет корректность работы сайта FUN&SUN
    с различными операциями по поиску и просмотру туров для отдыха.
   - **Шаги теста**:
     - Открытие страницы сайта FUN&SUN.
     - Закрытие всплывающих окон рекламы закрывающих видимость сайта.
     - Переход на страницу авторизации.
     - Ввод данных для авторизации.
     - Открытие меню авторизованного пользователя.
     - Просмотр информации о пользователе.
     - Ввод данных поиска тура.
         - Ввод данных поиска поля "Откуда".
         - Ввод данных поиска поля "Куда".
         - Ввод данных поиска поля "Дата вылета".
         - Ввод данных поиска поля "Количество ночей".
         - Ввод данных поиска поля "Кто едет".
     - Нажатие кнопки "Найти"     

   - **Результат**: Успешное выполнение или ошибка с указанием ожидаемого и фактического результата.
