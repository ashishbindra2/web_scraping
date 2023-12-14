import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestGoogleSearch:
    @pytest.fixture()
    def setup_teardown(self):
        global driver
        driver = webdriver.Firefox()
        driver.get('http://google.co.in')
        driver.maximize_window()

        yield
        time.sleep(5)
        driver.close()

    def test(self,setup_teardown):
        driver.find_element(By.NAME, 'q').send_keys('Mahesh Babu')
        time.sleep(5)
        driver.find_element(By.NAME, 'btnK').click()
        driver.find_element(By.CLASS_NAME, 'LC20lb').click()

