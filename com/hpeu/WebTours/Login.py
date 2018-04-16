# coding=utf-8

import time
import unittest
from selenium import webdriver
from com.hpeu.Tools.ReadFile import ReadFile
from lib2to3.tests.support import driver

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #driver = webdriver.Ie()
        self.GetVule = ReadFile()
    
    def test_WebTourLogin(self):
        mydriver = self.driver
        
        SystemURL =self.GetVule.getURL('WebToursSystem', 'SystemURL')
        Username = self.GetVule.getElement('NAME', 'UsernameInputBox')
        Password = self.GetVule.getElement('NAME', 'PasswordInputBox')
        Loginbtn = self.GetVule.getElement('NAME', 'LoginBtn')
        
        
        time.sleep(15)
        
        mydriver.get(SystemURL)
        
        time.sleep(5)
        #assert 'Register here to join Mercury Tours!' in mydriver.page_source
        
        mydriver.find_element_by_name(Username).send_keys('LuShiPeng')
        
        mydriver.find_element_by_name(Password).send_keys('lushipeng')
        
        mydriver.find_element_by_name(Loginbtn).click()
        
        #assert 'Use our Flight Finder to search for the lowest fare on participating airlines' in mydriver.page_source
        
        time.sleep(5)
        
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
'''     
if __name__ == '__main__':
    unittest.main()
'''        