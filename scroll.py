from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time
import unittest


class Scrolling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass method execution...')
        global driver
        driver = webdriver.Firefox()
        driver.get('https://www.monster.be/nl/vacatures/zoeken?q=it&where=&page=3&so=m.h.s')
        driver.maximize_window()

    @staticmethod
    def test_scroll_body():
        driver.execute_script("window.scrollTo(0,500)")

    @staticmethod
    def test_scroll_card():
        while True:
            time.sleep(2)
            # card = driver.find_element(By.ID, 'card-scroll-container')
            height = driver.execute_script("var scrollContainer = document.querySelector("
                                           "'.splitviewstyle__CardScrollContainer-sc-zpzpmg-2.fxBczI');"
                                           "return scrollContainer.scrollHeight"
                                           )
            print("height -->", height)
            driver.execute_script("var scrollContainer = document.querySelector("
                                  "'.splitviewstyle__CardScrollContainer-sc-zpzpmg-2.fxBczI');"
                                  "scrollContainer.scrollTo(0,scrollContainer.scrollHeight);"
                                  )
            driver.implicitly_wait(5)
            time.sleep(5)
            new_height = driver.execute_script("var scrollContainer = document.querySelector("
                                               "'.splitviewstyle__CardScrollContainer-sc-zpzpmg-2.fxBczI');"
                                               "return scrollContainer.scrollHeight"
                                               )

            print("new height -->", new_height)
            print("----------------------------")
            if height == new_height:
                break

    # @staticmethod
    # def test_logout():
    #     driver.find_element(By.XPATH,
    #                         '//div[@class="wp-block-group"]').click()
    #     time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # driver.close()
        pass


unittest.main()
