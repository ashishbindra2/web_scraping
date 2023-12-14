from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time
import unittest


class HMSLoginLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass method execution...')
        global driver
        driver = webdriver.Firefox()
        driver.get('https://practicetestautomation.com/practice-test-login/')
        driver.maximize_window()

    @staticmethod
    def test_login():
        driver.find_element(By.NAME, 'username').send_keys('student')
        driver.find_element(By.NAME, 'password').send_keys('Password123')
        driver.find_element(By.ID, 'submit').click()
        time.sleep(10)

    @staticmethod
    def test_logout():
        driver.find_element(By.XPATH,
                            '//div[@class="wp-block-group"]').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        driver.close()


unittest.main()
