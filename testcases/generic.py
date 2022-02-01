from selenium import webdriver
url ="https://nxtgenaiacademy.com/demo-site/"

import unittest

class GENERICLASS():
    driver = webdriver.Chrome()
    def setUp(self):

        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
