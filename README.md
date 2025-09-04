## Установка используемых библиотек
```bash
pip install -r requirements.txt
```

## Запуск тестов

По умолочанию используется **Chrome**.
Можно указать браузер и его версию:
```bash
pytest -v tests/ --browser=chrome
pytest -v tests/ --browser=firefox
pytest -v tests/ --browser=chrome --browser-version=121.0
pytest -v tests/
```

## Запуск тестов с результатами для Allure

```bash
pytest -v tests/ --alluredir=allure-results
```

### Быстрый просмотр 
```bash
allure serve allure-results
```

### Генерация и открытие статического отчета
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

