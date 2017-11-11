#!/usr/bin/python
# coding: utf-8 -*-

import codecs
#import unittest framework
import unittest
#importing webdriver from selenium
from selenium import webdriver
#importing keys to enter keyboard event
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):  # defining a class

    def setUp(self): # defining setup method / func
         #Launching chrome browser
         self.driver = webdriver.Chrome(executable_path=r'E:\py-selenium\drivers\chromedriver.exe')

    #test_search_in_python_org
    def test_search_url_links(self): #definng a test method

        #logfile
        logfile = codecs.open("links.txt",'w',encoding='utf-8')
        #Navigating to required website using get method
        driver = self.driver
        driver.get("https://pythonprogramming.net/")
        driver.implicitly_wait(10)   #Synchroniztion / wait
        elems = driver.find_elements_by_xpath("//a[@href]")
        mylinks = []
        for elem in elems:
            if not elem.get_attribute("href") in mylinks:
                mylinks.append(elem.get_attribute("href"))
        for lnk in mylinks:
            logfile.write(lnk + '\n')
        assert "No results found." not in driver.page_source

    def tearDown(self): #Defining a tear down method / cleaup activities
    #closing the browser
        self.driver.save_screenshot('href_screenshot.png') #take a screenshot()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()