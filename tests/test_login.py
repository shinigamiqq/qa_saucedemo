import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Проверка входа пользователя")
@allure.description("Тест проверяет возможность входа в систему под пользователем standard_user")
def test_login_valid_user(driver):
    with allure.step("Открыть страницу логина"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Ввести имя пользователя"):
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")

    with allure.step("Ввести пароль пользователя"):
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

    with allure.step("Нажать кнопку логин"):
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

    with allure.step("Проверить, что загружена страницу с товарами"):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")

        assert inventory_list.is_displayed(), "Список товаров не отображается после логина"

