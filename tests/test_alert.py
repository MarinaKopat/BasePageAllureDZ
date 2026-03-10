import allure
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = 'https://demo.automationtesting.in/Alerts.html'


@pytest.mark.only
@allure.feature('Работа с алертами')
class TestAlerts:

    @allure.title('Алерт с кнопкой OK')
    def test_alert_simple(self, driver):
        page = BasePage(driver)
        page.open(URL)

        page.click((By.CSS_SELECTOR, "[onclick='alertbox()']"))

        alert = driver.switch_to.alert
        assert alert.text == 'I am an alert box!'
        alert.accept()

    @allure.title('Алерт с отменой (Cancel)')
    def test_alert_cancel(self, driver):
        page = BasePage(driver)
        page.open(URL)

        page.click((By.LINK_TEXT, 'Alert with OK & Cancel'))
        page.click((By.CSS_SELECTOR, "[onclick='confirmbox()']"))

        alert = driver.switch_to.alert
        assert alert.text == 'Press a Button !'
        alert.dismiss()

        assert page.get_text((By.ID, 'demo')) == 'You Pressed Cancel'

    @allure.title('Алерт с вводом текста')
    def test_alert_input_text(self, driver):
        page = BasePage(driver)
        page.open(URL)

        page.click((By.LINK_TEXT, 'Alert with Textbox'))
        page.click((By.CSS_SELECTOR, '[onclick="promptbox()"]'))

        alert = driver.switch_to.alert
        name = 'Marina'
        alert.send_keys(name)
        alert.accept()

        assert name in page.get_text((By.ID, 'demo1'))
