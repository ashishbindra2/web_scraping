import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = None


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get('http://google.co.in')
        driver.maximize_window()

    def test(self):
        driver.find_element(By.NAME, 'q').send_keys('Mahesh Babu')
        time.sleep(5)
        driver.find_element(By.NAME, 'btnK').click()
        driver.find_element(By.CLASS_NAME, 'LC20lb').click()

    def tearDown(self):
        driver.close()


unittest.main()
