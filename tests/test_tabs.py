import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = 'https://demoqa.com/browser-windows'
TAB_BUTTON = (By.ID, 'tabButton')
SAMPLE_HEADING = (By.ID, 'sampleHeading')


@pytest.mark.only
@allure.feature('Browser Windows')
@allure.story('Tab Handling')
def test_tab(driver):
    page = BasePage(driver)

    page.open(URL)
    page.click(TAB_BUTTON)

    page.switch_to_window(1)

    with allure.step('Проверка текста на новой вкладке'):
        assert page.get_text(SAMPLE_HEADING) == 'This is a sample page'

    page.close_tab()

    page.switch_to_window(0)

    with allure.step('Проверка возврата на исходный URL'):
        assert driver.current_url == URL
