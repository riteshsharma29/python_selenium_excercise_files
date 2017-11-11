#!/usr/bin/python
# coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        #path for the chrome driver
        self.driver = webdriver.Chrome(executable_path=r'E:\py-selenium\drivers\chromedriver.exe')

        # path for the chrome driver
    def test_login(self):
        driver = self.driver
        driver.get("https://accounts.google.com/signin/v2/identifier?service")
        username = driver.find_element_by_id('identifierId')
        username.send_keys('my_usernam')
        time.sleep(2)
        driver.find_element_by_id('identifierNext').click()
        time.sleep(2)
        passwd = driver.find_element_by_name('password')
        passwd .send_keys('my_password')
        driver.find_element_by_id('passwordNext').click()
        time.sleep(5)

    def tearDown(self): #Defining a tear down method / cleaup activities
    #closing the browser
        self.driver.save_screenshot('screenshot.png') #take a screenshot()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
