import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox",
    )
    parser.addoption(
        "--browser-version",
        action="store",
        default=None,
        help="Версия браузера",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    browser_version = request.config.getoption("--browser-version")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Браузер {browser} не поддерживается. Используйте chrome или firefox.")

    if browser_version:
        print(f"Запуск в браузере: {browser}, версия: {browser_version}")
    else:
        print(f"Запуск в браузере: {browser}, версия: локальная")

    driver.maximize_window()
    yield driver
    driver.quit()

