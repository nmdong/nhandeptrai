'''
Created on Apr 28, 2020

@author: GI-LAB
'''

import time
from robot.api import logger
from selenium.webdriver.common.by import By
from time import sleep
from ultis.common.selenium import selenium
# from selenium import webdriver
# from ultis import driver
# from selenium.webdriver.remote.webelement import WebElement
from ultis.common.selenium_tools import selenium_tools

# from selenium.webdriver.common.action_chains import ActionChains


# from JmetterLibrary import JMeterLib
# from SOCKETBOT.CLIENTS.SOCKET_IMPLEMENTED import PTI_9611
# from SOCKETBOT.UTILITY import Function9611
# from SSHLibrary import library
# from SeleniumLibrary.keywords import formelement
# from SeleniumLibrary.keywords.formelement import FormElementKeywords

# from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver
# from web_app_packet.web_functions import web_functions

# from utilities_Py_packet import driver

class designer_console_page():
    '''this class will define all locators and function on Register Page'''
    
    def __init__(self):
        
        self.ED_LOGIN_DESIGNER_PAGE = "#loginouterdivWrapper"
        self.ED_DESIGNER_PAGE = "#naraTopMenu > div.narLeftMenuBtns > div > img" #CSS
        self.USERNAME_DESIGNER_PAGE_TF = "input#IDToken1" #CSS Selector
        self.PASSWORD_DESIGNER_PAGE_TF = "#IDToken2" #CSS Selector
        self.LOGON_DESIGNER_PAGE_BTN = "input#SubmitButton"
        self.IMPORT_WF_BTN = "button.narImportBtn"
        self.BROWSE_BTN = "input#importwfdfile"
        self.IMPORT_BTN = "button.propertyPageMainButtonM.ui-button.ui-widget.ui-state-default.ui-corner-all"
        self.SAVE_DROPDOWN = "#narWorkflowFileNameImg"
        self.SAVE_WF_BTN = "#narWfsavebox > div > div:nth-child(5) > label"
        self.SAVE_AS_BTN = "#narWfsavebox > div > div:nth-child(7) > label"
        self.VALIDATE_BTN = "#naraTopMenu > div.narRightMenuBtns > button:nth-child(1)"
        self.DEPLOY_BTN = "#naraTopMenu > div.narRightMenuBtns > button:nth-child(2)"
        self.ADMIN_CONSOLE_BTN = "#naraTopMenu > div.narRightMenuBtns > button:nth-child(4)"
        self.SAVED_FOLDER = "#AutoTest_anchor"
        self.SAVE_BTN = "#ext-gen16 > div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-box-custom.saveworkflow.ui-dialog-buttons.ui-draggable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(2) > span"
        self.SAVE_TOAST_MSG = ".toast-message"  
        self.WORKFLOW_NAME_TF = "#deployWfdFilename"    
        self.DEPLOY_COMFIRM_BTN = "button.propertyPageMainButtonO.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only > span"  
        self.IFTTT_TASK = "div.narnodetitle.narnodetitle_gold > div > img"
        self.NEW_RULE_SET_TF = "#NewRuleSet"
        self.CLOSE_TASK_PROPERTY_BTN = "#ext-gen202"
        self.PROPERTY_OPTION = "tr:nth-child(10) > td.mxPopupMenuItem"
        
        self.TEST = "#ext-gen16 > div.mxPopupMenu > table > tbody > tr:nth-child(10) > td.mxPopupMenuItem"
        self.WORKFLOW_NAME_DRAFT_TF = "#saveWfdWorkflowName"
#         self.old_tabs=None
#         self.new_tabs=None
      
        
    def load_login_designer_page(self, driver):

        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ED_LOGIN_DESIGNER_PAGE, 5):
            print("Passed ben POM")
            return True
        else:
            raise AssertionError("Failed! ben POM")
            return False
    
    def input_designer_username(self, driver,  username_register):
        username_tf = driver.find_element(By.CSS_SELECTOR, self.USERNAME_DESIGNER_PAGE_TF)
        username_tf.clear()
        username_tf.send_keys(username_register)
        logger.info("input username in ED Designer page successfully")
           
        
    def input_designer_password(self, driver, password_register):
        password_tf = driver.find_element(By.CSS_SELECTOR, self.PASSWORD_DESIGNER_PAGE_TF)
        password_tf.clear()
        password_tf.send_keys(password_register)
        logger.info("input password in ED Designer page successfully")
        
        
    def click_logon_button (self, driver):
        register_btn_element = driver.find_element(By.CSS_SELECTOR, self.LOGON_DESIGNER_PAGE_BTN)
        register_btn_element.click()
        
    def load_designer_page(self, driver):

        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ED_DESIGNER_PAGE, 10): # = time.sleep(10)
            print("Login ADmin page successfully")
            return True
        else:
            raise AssertionError("Not found new project button" + '\n\n\n')
            return  False
        
    def import_wfd(self, driver, locator, wfname):
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.IMPORT_WF_BTN, 10)
        import_wf_btn_element = driver.find_element(By.CSS_SELECTOR, self.IMPORT_WF_BTN)
        import_wf_btn_element.click()
        
        driver.find_element_by_css_selector(self.BROWSE_BTN).send_keys(locator+wfname+'.xml')
         
        import_btn_element = driver.find_element(By.CSS_SELECTOR, self.IMPORT_BTN)
        import_btn_element.click()
        
#         logger.info("import wf successfully")
        
    def save_wfd(self,driver, wfname):
            
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_DROPDOWN, 5)
        save_wf_dropdown_element = driver.find_element(By.CSS_SELECTOR, self.SAVE_DROPDOWN)
        save_wf_dropdown_element.click()  
        sleep(1)  
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_WF_BTN, 5)
        save_wf_btn_element = driver.find_element(By.CSS_SELECTOR, self.SAVE_WF_BTN)
        save_wf_btn_element.click()    
        sleep(1) 
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVED_FOLDER, 5)
        save_folder_element = driver.find_element(By.CSS_SELECTOR, self.SAVED_FOLDER)
        save_folder_element.click()    
        sleep(1)         
        
        workflow_name_DRAFT_tf = driver.find_element(By.CSS_SELECTOR, self.WORKFLOW_NAME_DRAFT_TF)
        workflow_name_DRAFT_tf.clear()
        workflow_name_DRAFT_tf.send_keys(wfname)
        sleep(1)
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_BTN, 5)
        save_btn_element = driver.find_element(By.CSS_SELECTOR, self.SAVE_BTN)
        save_btn_element.click()    
        sleep(1)  
        
        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_TOAST_MSG, 5):
            print("MESSGE IS SHOWN CORRECTLY")
            return True
        else:
            raise AssertionError("Failed! MESSAGE IS NOT SHOWN")
        
         
    def save_as_wfd(self, driver):
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_DROPDOWN, 5)
        save_wf_dropdown_element = driver.find_element(By.CSS_SELECTOR, self.SAVE_DROPDOWN)
        save_wf_dropdown_element.click()  
        sleep(2)  
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_AS_BTN, 5)
        save_as_wf_btn_element = driver.find_element(By.CSS_SELECTOR, self.SAVE_AS_BTN)
        save_as_wf_btn_element.click()      
        
    def validate_wfd(self, driver):
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.VALIDATE_BTN, 5)
        validate_btn_element = driver.find_element(By.CSS_SELECTOR, self.VALIDATE_BTN)
        validate_btn_element.click()  
        sleep(1)  
        
    def deploy_wfd(self, driver,wfname):   
        
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.DEPLOY_BTN, 5)
        deploy_btn_element = driver.find_element(By.CSS_SELECTOR, self.DEPLOY_BTN)
        deploy_btn_element.click() 
        sleep(1) 
        
        workflow_name_tf = driver.find_element(By.CSS_SELECTOR, self.WORKFLOW_NAME_TF)
        workflow_name_tf.clear()
        workflow_name_tf.send_keys(wfname)
        
        deploy_confirm_btn_element = driver.find_element(By.CSS_SELECTOR, self.DEPLOY_COMFIRM_BTN)
        deploy_confirm_btn_element.click() 
        sleep(1)
        
        
        
    def navigate_to_AdminConsole(self,driver):
        selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADMIN_CONSOLE_BTN, 5)
        navigate_admin_console_element = driver.find_element(By.CSS_SELECTOR, self.ADMIN_CONSOLE_BTN)
        navigate_admin_console_element.click()
        sleep(5)
#         print( "Tab(s) is openned: "+ str(len(driver.window_handles)))
#         driver.switch_to.window(driver.window_handles[1])

        
    def switch_tab(self,driver):
        print( "Tab(s) is opened: "+ str(len(driver.window_handles)))
        driver.switch_to.window(driver.window_handles[1])
        
        
        
#         driver.find_element(By.CSS_SELECTOR, self.WF_TAB).click()
#         driver.find_element(By.CSS_SELECTOR, self.REFRESH_WF_BTN).click()
#         
#         input_wfname_tf = driver.find_element(By.CSS_SELECTOR, self.WF_TF)
#         input_wfname_tf.clear()
#         input_wfname_tf.send_keys(wfname)
#         driver.find_element(By.CSS_SELECTOR, self.WF_CHECKBOX).click()
#         driver.find_element(By.CSS_SELECTOR, self.UNDEPLOY_WF_BTN).click()
        
#################################################################################################################

    def input_ruleset_IFTTT_task(self, driver, ruleset_name):
        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.IFTTT_TASK, 5):
            selenium_tools().double_click(driver,By.CSS_SELECTOR, self.IFTTT_TASK)
            
#             selenium_tools().right_click(driver,By.CSS_SELECTOR, self.IFTTT_TASK)

#             print(str(len(driver.window_handles)))    
#             driver.switch_to.window(driver.window_handles[0])     
#             selenium_tools().wait_for_element_appear(driver, By.CSS_SELECTOR, self.TEST, 10)  
#             driver.switch_to.window(driver.window_handles[1])
#             selenium_tools().wait_for_element_appear(driver, By.CSS_SELECTOR, self.TEST, 10)
#             driver.close();
#             driver.switch_to.window(driver.window_handles[0])
#             selenium_tools().click(driver, By.CSS_SELECTOR, self.PROPERTY_OPTION)       


            new_ruleset_tf = driver.find_element(By.CSS_SELECTOR, self.NEW_RULE_SET_TF)
            logger.info("STRAT INPUT NEW RULE SET NAME")
            new_ruleset_tf.clear()
            new_ruleset_tf.send_keys(ruleset_name)
            sleep(5)
            close_property = driver.find_element(By.CSS_SELECTOR, self.CLOSE_TASK_PROPERTY_BTN)
            close_property.click()
            
        else:
            print("TCs with this WFD does not have IFTTT TASK!!!")
            
####################################################################################################
        
            
            
            
        
        
        