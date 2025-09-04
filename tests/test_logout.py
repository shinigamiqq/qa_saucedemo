import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver):
    """Хелпер для логина"""
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )


@allure.title("Проверка выхода залогиненного пользователя")
@allure.description("Тест проверяет возможность выхода залогиненого пользователя standard_user")
def test_logout_user(driver):
    with allure.step("Залогинивание пользователя"):
        login(driver)

    with allure.step("Открыть меню"):
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

    with allure.step("Подождать появления кнопки Logout и кликнуть"):
        logout_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()

    with allure.step("Проверить, что загружена страница логина"):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        assert driver.find_element(By.ID, "login-button").is_displayed(), "Кнопка Login не отображается после выхода"

