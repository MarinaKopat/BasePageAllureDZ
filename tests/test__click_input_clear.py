import time
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


GOALS_BTN = (By.CSS_SELECTOR, 'button.task-goals-btn')
CLOSE_MODAL = (By.CSS_SELECTOR, 'button.modal-close-x')
PERIOD_BTN = (By.CSS_SELECTOR, 'button.period-btn')
PROMO_INPUT = (By.CSS_SELECTOR, '.promo-input-wrapper input')
APPLY_BTN = (By.CSS_SELECTOR, 'button.promo-apply-btn')
SUCCESS_MSG = (By.CSS_SELECTOR, '.promo-message.success')
HINT_BTN = (By.CSS_SELECTOR, 'button.promo-hint-btn')


@pytest.mark.only
@allure.feature('Subscription Page')
@allure.story('Проверка различных методов клика')
def test_all_click_methods(driver, base_page):
    base_page.open('http://localhost:3000/automation-lab/subscription')

    base_page.click(GOALS_BTN)
    time.sleep(2)
    base_page.click(CLOSE_MODAL)

    base_page.js_click(PERIOD_BTN)

    base_page.scroll_to(PROMO_INPUT)
    base_page.send_keys(PROMO_INPUT, 'ALWAYS')

    with allure.step('Применение промокода через Enter'):
        element = driver.find_element(*APPLY_BTN)
        element.send_keys(Keys.ENTER)

    with allure.step('Проверка сообщения об успехе'):
        msg = driver.find_element(*SUCCESS_MSG).text
        assert msg == 'Промокод применён: Скидка 15% для для всех тарифов'

    with allure.step('Клик через ActionChains'):
        actions = ActionChains(driver)
        hint_btn = driver.find_element(*HINT_BTN)
        actions.move_to_element(hint_btn).click().perform()
