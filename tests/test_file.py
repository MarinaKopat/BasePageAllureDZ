import os
import time
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = 'https://demoqa.com/upload-download'


@pytest.mark.only
@allure.feature('Upload and Download')
class TestFileOperations:

    @allure.title('Тест загрузки файла (Download)')
    @pytest.mark.download
    def test_download(self, driver):
        page = BasePage(driver)
        page.open(URL)

        download_btn = (By.ID, 'downloadButton')
        page.click(download_btn)

        time.sleep(3)
        with allure.step('Проверить, что переход на страницу загрузок выполнен'):
            driver.get('chrome://downloads/')
            assert 'chrome://downloads' in driver.current_url

    @allure.title('Тест выгрузки файла (Upload)')
    @pytest.mark.upload
    def test_upload(self, driver):
        page = BasePage(driver)
        page.open(URL)

        file_path = os.path.abspath('C:/Users/user/Desktop/DZQ22--Python-Automation/file/sampleFile.jpeg')
        upload_input = (By.ID, 'uploadFile')
        result_label = (By.ID, 'uploadedFilePath')

        page.send_keys(upload_input, file_path)

        result_text = page.get_text(result_label)

        with allure.step('Проверить имя загруженного файла'):
            assert 'sampleFile.jpeg' in result_text
            allure.attach(driver.get_screenshot_as_png(), name='Result', attachment_type=allure.attachment_type.PNG)
