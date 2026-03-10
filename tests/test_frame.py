import time
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = 'https://demoqa.com/frames'


@allure.feature('Frames')
@allure.story('Проверка текста внутри фрейма')
@pytest.mark.only
def test_frame(driver):
    page = BasePage(driver)

    page.open(URL)
    time.sleep(2)

    FRAME_1 = (By.ID, 'frame1')
    HEADING = (By.CSS_SELECTOR, '#sampleHeading')

    page.switch_to_frame(FRAME_1)

    with allure.step('Проверка соответствия текста'):
        text = page.get_text(HEADING)
        assert text == 'This is a sample page'

    page.switch_to_default()
