import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step
    def open(self, url):
        self.driver.get(url)

    @allure.step
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step
    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step
    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step
    def switch_to_frame(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(element)

    @allure.step
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    @allure.step
    def switch_to_window(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    @allure.step
    def close_tab(self):
        self.driver.close()
