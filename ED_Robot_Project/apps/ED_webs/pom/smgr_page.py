'''
Created on Apr 28, 2020

@author: GI-LAB
'''

import time
from robot.api import logger
from selenium.webdriver.common.by import By
from time import sleep
from ultis.common.selenium import selenium

# from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver
# from web_app_packet.web_functions import web_functions

# from utilities_Py_packet import driver

class smgr_page():
    '''this class will define all locators and function on Register Page'''
    
    def __init__(self):
        
        self.SGMR_PAGE = "#r1_app_shell" #CSS
        self.USERNAME_TF = "#j_username" #CSS Selector
        self.PASSWORD_TF = "#j_password" #CSS Selector
        self.LOGON_BTN = "#SubmitButton"
        self.PRIVACY_TXT = "#main-message > h1"
#         self.ADVANCED_BTN = "button#details-button"
#         self.PROCEED_BTN = "#proceed-link"
   
                
      
        
    def load_login_page(self, driver):
#         smgr_page_element = driver.find_elements(By.CSS_SELECTOR, self.SGMR_PAGE)
#         i = 0
#         while i > 10:
#             i = i+1
#             time.sleep(10)
#             if smgr_page_element.length() > 0:
#                 return True
#             else:
#                 raise AssertionError("failed")
#                 print("Not found smgr page")
#                 return False
            
        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SGMR_PAGE, 5):
            print("Passed ben POM")
            return True
        else:
            raise AssertionError("Failed! ben POM")
            return False
     
    def input_smgr_username(self, driver,  username_register):
        username_tf = driver.find_element(By.CSS_SELECTOR, self.USERNAME_TF)
        username_tf.clear()
        username_tf.send_keys(username_register)
        logger.info("input username in SMRG page successfully")
           
        
    def input_smgr_password(self, driver, password_register):
        password_tf = driver.find_element(By.CSS_SELECTOR, self.PASSWORD_TF)
        password_tf.clear()
        password_tf.send_keys(password_register)
        logger.info("input password in SMGR page successfully")
        
        
    def click_logon_button (self, driver):
        register_btn_element = driver.find_element(By.CSS_SELECTOR, self.LOGON_BTN)
        register_btn_element.click()
        