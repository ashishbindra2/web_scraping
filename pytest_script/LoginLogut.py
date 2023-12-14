from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time
import pytest


class TestLoginLogout:
    @pytest.fixture(scope='module')
    def setup_teardown_class(self):
        print('setUpClass method execution...')
        global driver
        driver = webdriver.Firefox()
        driver.get('https://practicetestautomation.com/practice-test-login/')
        driver.maximize_window()

        yield
        driver.close()

    @staticmethod
    def test_login(setup_teardown_class):
        driver.find_element(By.NAME, 'username').send_keys('student')
        driver.find_element(By.NAME, 'password').send_keys('Password123')
        driver.find_element(By.ID, 'submit').click()
        time.sleep(10)

    @staticmethod
    def test_logout(setup_teardown_class):
        driver.find_element(By.XPATH,
                            '//div[@class="wp-block-group"]').click()
        time.sleep(2)

