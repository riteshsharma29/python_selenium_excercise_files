#!/usr/bin/python
# coding: utf-8 -*-

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import codecs

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
         self.driver = webdriver.Chrome(executable_path=r'E:\py-selenium\drivers\chromedriver.exe')

    def test_count_unreadmsg(self):

         log_file = codecs.open("google_results.txt","w",encoding='utf-8')

         driver = self.driver
         #search python selenium in the Google search box
         results = driver.get('https://www.google.com/search?q=python selenium')
         html = driver.page_source

         soup = bs(html,"lxml")

         log_file.write('\n' + "######################## Search results : title ########################" + '\n' + '\n')

         for title in soup.find_all('h3'):
             #print title.text
             log_file.write(title.text + '\n')

         log_file.write('\n' + "######################## Search results : URL ########################" + '\n' + '\n')

         for link_text in soup.find_all('cite'):
             #print link_text.text
             log_file.write(link_text.text + '\n')

         log_file.write('\n' + "######################## Search results : description ########################" + '\n' + '\n')

         spans = soup.find_all('span', {'class': 'st'})
         # create a list of lines corresponding to element texts
         lines = [span.get_text() for span in spans]

         for desc in lines:
             #print desc
             log_file.write(desc + '\n')


    def tearDown(self): #Defining a tear down method / cleaup activities
        self.driver.save_screenshot('screenshot.png') #take a screenshot()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()