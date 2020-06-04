'''
Created on Apr 28, 2020

@author: GI-LAB
'''

import time
from robot.api import logger
from selenium.webdriver.common.by import By
from time import sleep
from ultis.common.selenium import selenium
from ultis.common.selenium_tools import selenium_tools
from telnetlib import SE

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.ui import Select

# from SSHLibrary import SSHClient
# from SSHLibrary import SSHLibrary
# from SSHLibrary import abstractclient
# from SSHLibrary import pythonclient
# from SSHLibrary.pythonclient import PythonSSHClient

# from lib2to3.pgen2.driver import Driver
# from lib2to3.tests.support import driver
# from web_app_packet.web_functions import web_functions

# from utilities_Py_packet import driver

class admin_console_page():
    '''this class will define all locators and function on Register Page'''
    
    def __init__(self):
        
        self.ED_LOGIN_ADMIN_PAGE = "#loginouterdivWrapper"
        self.ED_ADMIN_PAGE = "div.navbar-header.col-sm-7 > a > img" #CSS
        self.USERNAME_ADMIN_PAGE_TF = "input#IDToken1" #CSS Selector
        self.PASSWORD_ADMIN_PAGE_TF = "#IDToken2" #CSS Selector
        self.LOGON_ADMIN_PAGE_BTN = "input#SubmitButton"
        
        self.WF_TAB = "#workflowLi > a"
        self.REFRESH_WF_BTN = "#workflow > div.bootstrap-table > div.fixed-table-toolbar > div.columns.columns-right.btn-group.pull-right > button"
        self.WF_CHECKBOX = "#tableWorkflow > thead > tr > th.bs-checkbox > div.th-inner > label > input[type=checkbox]"
        self.WF_TF = "#workflow > div.bootstrap-table > div.fixed-table-toolbar > div.pull-right.search > input"
        self.UNDEPLOY_WF_BTN = "button#undeploywfdId"
        self.CONFIRM_UNDEPLOY_WF_BTN = "button#confirmUndeployWfd"
        self.UNDEPLOY_TOAST_MSG = ".toast-message"
        
        self.WF_DRAFT_TAB = "#wfdLi > a"
        self.REFRESH_WF_DRAFT_BTN = "#wfd > div.bootstrap-table > div.fixed-table-toolbar > div.columns.columns-right.btn-group.pull-right > button"
        self.WF_DRAFT_CHECKBOX = "#tableWfd > thead > tr > th.bs-checkbox > div.th-inner > label > input[type=checkbox]"
        self.WF_DARFT_TF = "#wfd > div.bootstrap-table > div.fixed-table-toolbar > div.pull-right.search > input"
        self.DELETE_WF_DRAFT_BTN = "button#deleteWfd"
        self.CONFIRM_DELETE_WF_DRAFT_BTN = "button#confirmDeleteWfd"
        
        self.RULES_TAB = "#rulesLi > a"
        self.REFRESH_RULES_BTN = "#rules > div.bootstrap-table > div.fixed-table-toolbar > div.columns.columns-right.btn-group.pull-right > button"
        self.RULES_CHECKBOX = "#tableRules > thead > tr > th.bs-checkbox > div.th-inner > label > input[type=checkbox]"
        self.RULES_TF = "#rules > div.bootstrap-table > div.fixed-table-toolbar > div.pull-right.search > input"
        self.OK_DELETE_BTN = "body > div.bootbox.modal.fade.bootbox-confirm.in > div > div > div.modal-footer > button.btn.btn-success.bootbox-accept"
        self.RULES_DELETE_BTN = "#toolbarTableRules > div:nth-child(3) > button"
        self.RULES_EDIT_BTN = "#toolbarTableRules > div:nth-child(2) > button"
        
        self.SELECT_WFD_DROPDOWN = "#createRuleSetModelBody > div:nth-child(1) > div > span:nth-child(2) > div > button"
        
        self.ADD_RULE_BTN = "button#addRule_ruleset_btn"
        self.SET_RULE_NAME_TF = "a#rule_Name"
        self.RULE_NAME_TF = "div:nth-child(1) > div.editable-input > input"
        self.SET_RULE_NAME_TICK_ICON = "#ruleEditorCond > div:nth-child(1) > span > span > div > form > div > div:nth-child(1) > div.editable-buttons > button.btn.btn-primary.btn-sm.editable-submit > i"
        
        self.SELECT_VARIABLE_DROPDOWN_1 = "#ruleEdi_simple_exp > div > div:nth-child(1) > button"
        self.CALLING_NUMBER_VARIABLE = "#ruleEdi_simple_exp > div > div.btn-group.bootstrap-select.open > div > ul > li:nth-child(9) > a > span.text"
        self.HTTP_CALLING_NUMBER_VARIABLE = "#ruleEdi_simple_exp > div > div.btn-group.bootstrap-select.open > div > ul > li:nth-child(15) > a"
        self.TEST = "div.btn-group.bootstrap-select.open > div > ul > li:nth-child(12)"
        
        self.SELECT_FUNCTION_DROPDOWN_1 = "#ruleEdi_simple_exp > div > div:nth-child(2) > button"
        self.EQUAL_TO_FUNCTION_1 = "#ruleEdi_simple_exp > div > div.btn-group.bootstrap-select.open > div > ul > li:nth-child(2) > a"
        self.ENTER_VALUE_TF_1 = "input#ruleEdi_value"
        
        
        self.ADD_CONDITION_BTN = "#ruleEdi_simple_exp > div > span.glyphicon.glyphicon-plus.text-success"
        
        self.SELECT_VARIABLE_DROPDOWN_2 = "#ruleEdi_simple_exp > div:nth-child(2) > div:nth-child(1) > div.btn-group.bootstrap-select > button"
        self.VIP_VARIABLE = "#ruleEdi_simple_exp > div:nth-child(2) > div:nth-child(1) > div.btn-group.bootstrap-select.open > div > ul > li:nth-child(13) > a"
        self.HTTP_VIP_VARIABLE = "#ruleEdi_simple_exp > div:nth-child(2) > div:nth-child(1) > div.btn-group.bootstrap-select.open > div > ul > li:nth-child(14) > a"
        self.SELECT_FUNCTION_DROPDOWN_2 = "#ruleEdi_simple_exp > div:nth-child(2) > div:nth-child(2) > div.btn-group.bootstrap-select > button"
        self.EQUAL_TO_FUNCTION_2 = "#ruleEdi_simple_exp > div:nth-child(2) > div:nth-child(2) > div.btn-group.bootstrap-select.open > div > ul > li:nth-child(2) > a"
        self.ENTER_VALUE_TF_2 = "input#ruleEdi_value1"
        
        self.ADD_MORE_BTN = "button#addrule_ruleset"
        
        self.THEN_SELECT_VARIABLE_DROPDOWN_1 = "#thenContainerBox > div > div > button"
        self.PROMPT_VARIABLE = "#thenContainerBox > div > div > div > ul > li:nth-child(2) > a"
        self.THEN_ENTER_VALUE_TF = "#thenContainerBox > div > input[type=text]"
        
        self.SAVE_RULE_BTN = "#addrule_saveRule"
        self.SAVE_DONE_BTN = "button#addruleset_saveRule"
        
        self.ROUTING_TAB = "#routingLi > a"
        self.ROUTING_REFRESH_BTN = "#routing > div.bootstrap-table > div.fixed-table-toolbar > div.columns.columns-right.btn-group.pull-right > button > i"
        self.ROUTING_SEARCH_TF = "#routing > div.bootstrap-table > div.fixed-table-toolbar > div.pull-right.search > input"
        self.ROUTING_CHECKBOX = "#tableRouting > thead > tr > th.bs-checkbox > div.th-inner > label > input[type=checkbox]"
        self.ROUTING_CREATE_BTN = "button#createRoutingRule"
        self.ROUTING_EDIT_BTN = "button#editRoutingRule"
        self.ROUTING_DELETE_BTN = "button#deleteRoutingRule"
        self.ROUTING_DELETE_CONFIRM_BTN = "button#deleteRuleConfirm"
        self.ROUTING_SELECT_EVENT_DROPDOWN = "#rulesPanelHeading > div:nth-child(1) > button"
        self.ROUTING_CALLINTERCEPT_CALLED = "#rulesPanelHeading > div.btn-group.bootstrap-select.show-tick.showHideHeadPanel.open > div > ul > li:nth-child(12) > a"
        self.ROUTING_SELECT_WORKFLOW_DROPDOWN = "#rulesPanelHeading > div:nth-child(2) > button"
        self.ROUTING_SELECT_WORKFLOW_TF = "#rulesPanelHeading > div.btn-group.bootstrap-select.show-tick.showHideHeadPanel.open > div > div > input"
        self.ROUTING_SELECT_WORKFLOW_SECTION = "#rulesPanelHeading > div.btn-group.bootstrap-select.show-tick.showHideHeadPanel.open > div > ul > li.active > a"
#         self.ROUTING_SELECT_WORKFLOW_SECTION = "#rulesPanelHeading > div.btn-group.bootstrap-select.show-tick.showHideHeadPanel.open > div > ul > li:nth-child(1) > a"
        self.ROUTING_ENTER_RULENAME_TF = "input#ruleName"
        self.ROUTING_ENTER_PRIORITY_TF = "input#rulePriority"
        self.ROUTING_ADD_RULE_BTN = "button#addRuleOption"
        self.ROUTING_SELECT_SCHEMA_ATTRIBUTE_DROPDOWN = "#rulesRow1 > td > div.btn-group.bootstrap-select.show-tick.eventSchemaDrop > button"
        self.ROUTING_CALLED_PARTY_EVENT_SECTION = "body > div.bs-container.btn-group.bootstrap-select.show-tick.eventSchemaDrop.open > div > ul > li:nth-child(7) > a"
        self.ROUTING_SELECT_FUNCTION_DROPDOWN = "#rulesRow1 > td > div.btn-group.bootstrap-select.show-tick.eventFunctionDrop > button"
        self.ROUTING_EQUAL_TO_FUNCTION = "body > div.bs-container.btn-group.bootstrap-select.show-tick.eventFunctionDrop.open > div > ul > li:nth-child(1) > a"
        self.ROUTING_ENTER_VALUE_TF = "input#valuebox1"
        self.ROUTING_SAVE_BTN = "button#saveRoutingRule"
        self.ROUTING_CALLINTERCEPT_CALLING = "#rulesPanelHeading > div.btn-group.bootstrap-select.show-tick.showHideHeadPanel.open > div > ul > li:nth-child(11) > a"
        self.ROUTING_CALLING_PARTY_EVENT_SECTION = "body > div.bs-container.btn-group.bootstrap-select.show-tick.eventSchemaDrop.open > div > ul > li:nth-child(3) > a"
        
        
        
        
        self.INSTENCES_TAB = "#instanceLi > a"
        self.INSTENCES_REFRESH_BTN = "#instance > div.bootstrap-table > div.fixed-table-toolbar > div.columns.columns-right.btn-group.pull-right > button > i"
        self.INSTENCES_SEARCH_TF = "input#searchInstances"
        self.INSTENCES_WF_NAME = "#tableInstance > tbody > tr > td:nth-child(5) > a"
        self.INSTENCES_STATE = "#tableInstance > tbody > tr > td:nth-child(7) > a"
        self.INSTENCES_DETAIL_CLOSE_BTN = "a > button"
        
      
      
        
    def load_login_admin_page(self, driver):
#         login_admin_page_element = driver.find_elements(By.CSS_SELECTOR, self.ED_LOGIN_ADMIN_PAGE)
#         i = 0
#         while i > 10:
#             i = i+1
#             time.sleep(10)
#             if login_admin_page_element.length() > 0:
#                 return True
#             else:
#                 print("Not found ED Admin login page")
#         return False
        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ED_LOGIN_ADMIN_PAGE, 10):
            print("Passed ben POM")
            return True
        else:
            raise AssertionError("Failed! ben POM")
            return False
    
    def input_admin_username(self, driver,  username_register):
        username_tf = driver.find_element(By.CSS_SELECTOR, self.USERNAME_ADMIN_PAGE_TF)
        username_tf.clear()
        username_tf.send_keys(username_register)
        logger.info("input username in ED Admin page successfully")
           
        
    def input_admin_password(self, driver, password_register):
        password_tf = driver.find_element(By.CSS_SELECTOR, self.PASSWORD_ADMIN_PAGE_TF)
        password_tf.clear()
        password_tf.send_keys(password_register)
        logger.info("input password in ED Admin page successfully")
        
        
    def click_logon_button (self, driver):
        register_btn_element = driver.find_element(By.CSS_SELECTOR, self.LOGON_ADMIN_PAGE_BTN)
        register_btn_element.click()
        
    def load_admin_page(self, driver):

        if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ED_ADMIN_PAGE, 10): # = time.sleep(10)
            print("Login ADmin page successfully")
            return True
        else:
            raise AssertionError("Not found new project button" + '\n\n\n')
            return  False
        
    def sshServer (self):
        print("ssh to server 100.20.128.60")
#         PythonSSHClient().enable_logging("100.20.128.60")
#         PythonSSHClient().login(username, password, allow_agent, look_for_keys, delay, proxy_cmd)

    def edit_rules_callintercept (self,driver,ruleset_name,extension1, Yes_or_No, prompt,calling_or_called ):
        print("strat edit Rules")
        

        driver.refresh()
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.RULES_TAB).click()
            
            driver.find_element(By.CSS_SELECTOR, self.REFRESH_RULES_BTN).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_TF, 10)
            input_RULES_tf = driver.find_element(By.CSS_SELECTOR, self.RULES_TF)
            input_RULES_tf.clear()
            input_RULES_tf.send_keys(ruleset_name)      
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_CHECKBOX, 10)
            rules_checkbox = driver.find_element(By.CSS_SELECTOR, self.RULES_CHECKBOX)
            rules_checkbox.click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_EDIT_BTN, 10)
            edit_rules = driver.find_element(By.CSS_SELECTOR, self.RULES_EDIT_BTN)
            edit_rules.click()
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADD_RULE_BTN, 10)
            add_rule = driver.find_element(By.CSS_SELECTOR, self.ADD_RULE_BTN)
            add_rule.click()

            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SET_RULE_NAME_TF, 10)
            driver.find_element(By.CSS_SELECTOR, self.SET_RULE_NAME_TF).click()

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULE_NAME_TF, 10)
            input_RULES_NAME_tf = driver.find_element(By.CSS_SELECTOR, self.RULE_NAME_TF)
            input_RULES_NAME_tf.clear()
            input_RULES_NAME_tf.send_keys(ruleset_name)
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SET_RULE_NAME_TICK_ICON, 10)
            driver.find_element(By.CSS_SELECTOR, self.SET_RULE_NAME_TICK_ICON).click()
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_1).click()
#             sleep(5)       
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.CALLING_NUMBER_VARIABLE, 10)
#             driver.find_element(By.CSS_SELECTOR, self.CALLING_NUMBER_VARIABLE).click()
            #After click dropdown, it will display selector for select (it is used commonly for the others dropdown on this page)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, "div.btn-group.bootstrap-select.open > select[data-title='Select variable']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.open > select[data-title='Select variable']"))
#             select.select_by_index(17)
            select.select_by_visible_text(calling_or_called)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_1).click()  
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_1).click()   
#             sleep(5)

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ENTER_VALUE_TF_1, 10)
            input_VALUE1_tf = driver.find_element(By.CSS_SELECTOR, self.ENTER_VALUE_TF_1)
            input_VALUE1_tf.clear()
            input_VALUE1_tf.send_keys(extension1)    
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADD_CONDITION_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ADD_CONDITION_BTN).click() 
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_2, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_2).click()  
#             sleep(5)          
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.VIP_VARIABLE, 10)
#             driver.find_element(By.CSS_SELECTOR, self.VIP_VARIABLE).click() 
#             sleep(5)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, "div.btn-group.bootstrap-select.open > select[data-title='Select variable']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.open > select[data-title='Select variable']"))
            select.select_by_visible_text('GlobalVariables.VIP')
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_2, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_2).click()  
#             sleep(5) 
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_2, 10)
            driver.find_element(By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_2).click()  
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ENTER_VALUE_TF_2, 10)
            input_VALUE2_tf = driver.find_element(By.CSS_SELECTOR, self.ENTER_VALUE_TF_2)
            input_VALUE2_tf.clear()
            input_VALUE2_tf.send_keys(Yes_or_No)   
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADD_MORE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ADD_MORE_BTN).click()  
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.THEN_SELECT_VARIABLE_DROPDOWN_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.THEN_SELECT_VARIABLE_DROPDOWN_1).click() 
#             sleep(5)
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.PROMPT_VARIABLE, 10)
#             driver.find_element(By.CSS_SELECTOR, self.PROMPT_VARIABLE).click() 
#             sleep(5)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, "div.btn-group.bootstrap-select.open > select[data-title='Select variable']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.open > select[data-title='Select variable']"))
            select.select_by_visible_text('Prompt.welcome')
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.THEN_ENTER_VALUE_TF, 10)
            input_THEN_VALUE_tf = driver.find_element(By.CSS_SELECTOR, self.THEN_ENTER_VALUE_TF)
            input_THEN_VALUE_tf.clear()
            input_THEN_VALUE_tf.send_keys(prompt)   
#             sleep(5)
            
                        
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_RULE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.SAVE_RULE_BTN).click() 
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_DONE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.SAVE_DONE_BTN).click()       
#             sleep(5)     
                         
   
        except:
            raise AssertionError("Failed edit rule") 
        
        
    def edit_rules_http (self,driver,ruleset_name,extension1, Yes_or_No, prompt, calling_or_called ):
        print("strat edit Rules HTTP")
        

        driver.refresh()
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.RULES_TAB).click()
            
            driver.find_element(By.CSS_SELECTOR, self.REFRESH_RULES_BTN).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_TF, 10)
            input_RULES_tf = driver.find_element(By.CSS_SELECTOR, self.RULES_TF)
            input_RULES_tf.clear()
            input_RULES_tf.send_keys(ruleset_name)      
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_CHECKBOX, 10)
            rules_checkbox = driver.find_element(By.CSS_SELECTOR, self.RULES_CHECKBOX)
            rules_checkbox.click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_EDIT_BTN, 10)
            edit_rules = driver.find_element(By.CSS_SELECTOR, self.RULES_EDIT_BTN)
            edit_rules.click()
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADD_RULE_BTN, 10)
            add_rule = driver.find_element(By.CSS_SELECTOR, self.ADD_RULE_BTN)
            add_rule.click()

            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SET_RULE_NAME_TF, 10)
            driver.find_element(By.CSS_SELECTOR, self.SET_RULE_NAME_TF).click()

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULE_NAME_TF, 10)
            input_RULES_NAME_tf = driver.find_element(By.CSS_SELECTOR, self.RULE_NAME_TF)
            input_RULES_NAME_tf.clear()
            input_RULES_NAME_tf.send_keys(ruleset_name)
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SET_RULE_NAME_TICK_ICON, 10)
            driver.find_element(By.CSS_SELECTOR, self.SET_RULE_NAME_TICK_ICON).click()
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_1).click()
            #After click dropdown, it will display selector for select (it is used commonly for the others dropdown on this page)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, "div.btn-group.bootstrap-select.open > select[data-title='Select variable']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.open > select[data-title='Select variable']"))
#             select.select_by_index(17)
#             select.select_by_visible_text('StartSchema.CallingParty')
            select.select_by_visible_text(calling_or_called)

#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.HTTP_CALLING_NUMBER_VARIABLE, 10)
#             driver.find_element_by_css_selector(self.HTTP_CALLING_NUMBER_VARIABLE)
#             driver.find_element(By.CSS_SELECTOR, self.HTTP_CALLING_NUMBER_VARIABLE).click()
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_1).click()  
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_1).click()   
#             sleep(5)

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ENTER_VALUE_TF_1, 10)
            input_VALUE1_tf = driver.find_element(By.CSS_SELECTOR, self.ENTER_VALUE_TF_1)
            input_VALUE1_tf.clear()
            input_VALUE1_tf.send_keys(extension1 + "@hcm.com")    
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADD_CONDITION_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ADD_CONDITION_BTN).click() 
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_2, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_VARIABLE_DROPDOWN_2).click()  
#             sleep(5)                  
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.HTTP_VIP_VARIABLE, 10)
#             driver.find_element(By.CSS_SELECTOR, self.HTTP_VIP_VARIABLE).click() 
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, "div.btn-group.bootstrap-select.open > select[data-title='Select variable']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.open > select[data-title='Select variable']"))
            select.select_by_visible_text('GlobalVariables.VIP')
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_2, 10)
            driver.find_element(By.CSS_SELECTOR, self.SELECT_FUNCTION_DROPDOWN_2).click()  
#             sleep(5) 
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_2, 10)
            driver.find_element(By.CSS_SELECTOR, self.EQUAL_TO_FUNCTION_2).click()  
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ENTER_VALUE_TF_2, 10)
            input_VALUE2_tf = driver.find_element(By.CSS_SELECTOR, self.ENTER_VALUE_TF_2)
            input_VALUE2_tf.clear()
            input_VALUE2_tf.send_keys(Yes_or_No)   
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ADD_MORE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ADD_MORE_BTN).click()  
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.THEN_SELECT_VARIABLE_DROPDOWN_1, 10)
            driver.find_element(By.CSS_SELECTOR, self.THEN_SELECT_VARIABLE_DROPDOWN_1).click() 
#             sleep(5)
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.PROMPT_VARIABLE, 10)
#             driver.find_element(By.CSS_SELECTOR, self.PROMPT_VARIABLE).click() 
#             sleep(5)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, "div.btn-group.bootstrap-select.open > select[data-title='Select variable']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.open > select[data-title='Select variable']"))
            select.select_by_visible_text('Prompt.welcome')
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.THEN_ENTER_VALUE_TF, 10)
            input_THEN_VALUE_tf = driver.find_element(By.CSS_SELECTOR, self.THEN_ENTER_VALUE_TF)
            input_THEN_VALUE_tf.clear()
            input_THEN_VALUE_tf.send_keys(prompt)   
#             sleep(5)
            
                        
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_RULE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.SAVE_RULE_BTN).click() 
#             sleep(5)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_DONE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.SAVE_DONE_BTN).click()       
#             sleep(5)     
                         
   
        except:
            raise AssertionError("Failed edit rule") 
        
        
    def add_route_called_party(self,driver,wfname, routing_name, PRIORITY, EXTENSION2):
        print("start add routing for called party")
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_TAB).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_REFRESH_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_REFRESH_BTN).click()   

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CREATE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_CREATE_BTN).click()
#             sleep(2)

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_EVENT_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_EVENT_DROPDOWN).click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR,"div.btn-group.bootstrap-select.show-tick.showHideHeadPanel > select[data-title='Select event']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.show-tick.showHideHeadPanel > select[data-title='Select event']"))
            select.select_by_visible_text('CallIntercepted-CALL_INTERCEPT_TO_CALLED_PARTY-1.0')
             
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CALLINTERCEPT_CALLED, 10)
#             driver.find_element(By.CSS_SELECTOR, self.ROUTING_CALLINTERCEPT_CALLED).click()
#             sleep(2)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_DROPDOWN).click()  
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_TF, 10)
            input_WF_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_TF)
            input_WF_tf.clear()
            input_WF_tf.send_keys(wfname +":latest")
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_SECTION, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_SECTION).click()           
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ENTER_RULENAME_TF, 10)
            input_RULENAME_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_ENTER_RULENAME_TF)
            input_RULENAME_tf.clear()
            input_RULENAME_tf.send_keys(routing_name)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ENTER_PRIORITY_TF, 10)
            input_PRIORRITY_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_ENTER_PRIORITY_TF)
            input_PRIORRITY_tf.clear()
            input_PRIORRITY_tf.send_keys(PRIORITY)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ADD_RULE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_ADD_RULE_BTN).click() 
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_SCHEMA_ATTRIBUTE_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_SCHEMA_ATTRIBUTE_DROPDOWN).click()
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CALLED_PARTY_EVENT_SECTION, 10)
#             driver.find_element(By.CSS_SELECTOR, self.ROUTING_CALLED_PARTY_EVENT_SECTION).click() 
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR,"div.btn-group.bootstrap-select.show-tick.eventSchemaDrop > select[data-title='Select schema attribute']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.show-tick.eventSchemaDrop > select[data-title='Select schema attribute']"))
            select.select_by_visible_text('CallEvent.calledParty.handle:string')
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_FUNCTION_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_FUNCTION_DROPDOWN).click()    
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_EQUAL_TO_FUNCTION, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_EQUAL_TO_FUNCTION).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ENTER_VALUE_TF, 10)
            input_VALUE_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_ENTER_VALUE_TF)
            input_VALUE_tf.clear()
            input_VALUE_tf.send_keys(EXTENSION2)
        
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SAVE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SAVE_BTN).click()              
            
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG, 10)    
            a = selenium_tools().getText(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG) 
            print(str(a))
            if a != "Saved Routing Rule.":
                
    #           if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_TOAST_MSG, 5):
                raise AssertionError("Failed! MESSAGE IS NOT SHOWN")
            else:
                print("MESSGE IS SHOWN CORRECTLY")
        
        except:
            raise AssertionError("Failed TO CREATE ROUTING RULE")
        
    def add_route_calling_party(self,driver,wfname, routing_name, PRIORITY, EXTENSION1):
        print("start add routing for calling party")
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_TAB).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_REFRESH_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_REFRESH_BTN).click()   

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CREATE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_CREATE_BTN).click()
#             sleep(2)

            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_EVENT_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_EVENT_DROPDOWN).click()
#             sleep(2)
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CALLINTERCEPT_CALLING, 10)
#             driver.find_element(By.CSS_SELECTOR, self.ROUTING_CALLINTERCEPT_CALLING).click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR,"div.btn-group.bootstrap-select.show-tick.showHideHeadPanel > select[data-title='Select event']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.show-tick.showHideHeadPanel > select[data-title='Select event']"))
            select.select_by_visible_text('CallIntercepted-CALL_INTERCEPT_FROM_CALLING_PARTY-1.0')
            
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_DROPDOWN).click()  
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_TF, 10)
            input_WF_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_TF)
            input_WF_tf.clear()
            input_WF_tf.send_keys(wfname +":latest")
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_SECTION, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_WORKFLOW_SECTION).click()           
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ENTER_RULENAME_TF, 10)
            input_RULENAME_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_ENTER_RULENAME_TF)
            input_RULENAME_tf.clear()
            input_RULENAME_tf.send_keys(routing_name)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ENTER_PRIORITY_TF, 10)
            input_PRIORRITY_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_ENTER_PRIORITY_TF)
            input_PRIORRITY_tf.clear()
            input_PRIORRITY_tf.send_keys(PRIORITY)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ADD_RULE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_ADD_RULE_BTN).click() 
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_SCHEMA_ATTRIBUTE_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_SCHEMA_ATTRIBUTE_DROPDOWN).click()
#             selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CALLING_PARTY_EVENT_SECTION, 10)
#             driver.find_element(By.CSS_SELECTOR, self.ROUTING_CALLING_PARTY_EVENT_SECTION).click() 
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR,"div.btn-group.bootstrap-select.show-tick.eventSchemaDrop > select[data-title='Select schema attribute']", 10)
            select = Select(driver.find_element_by_css_selector("div.btn-group.bootstrap-select.show-tick.eventSchemaDrop > select[data-title='Select schema attribute']"))
            select.select_by_visible_text('CallEvent.callingParty.handle:string')
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SELECT_FUNCTION_DROPDOWN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SELECT_FUNCTION_DROPDOWN).click()    
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_EQUAL_TO_FUNCTION, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_EQUAL_TO_FUNCTION).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_ENTER_VALUE_TF, 10)
            input_VALUE_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_ENTER_VALUE_TF)
            input_VALUE_tf.clear()
            input_VALUE_tf.send_keys(EXTENSION1)
        
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SAVE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_SAVE_BTN).click()              
            
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG, 10)    
            a = selenium_tools().getText(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG) 
            print(str(a))
            if a != "Saved Routing Rule.":
                
    #           if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_TOAST_MSG, 5):
                raise AssertionError("Failed! MESSAGE IS NOT SHOWN")
            else:
                print("MESSGE IS SHOWN CORRECTLY")
        
        except:
            raise AssertionError("Failed TO CREATE ROUTING RULE")        
        
    def check_wf_instences(self, driver, wfname):
        print("start checking WFD INSTENCES")
        driver.refresh()
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.INSTENCES_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.INSTENCES_TAB).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.INSTENCES_REFRESH_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.INSTENCES_REFRESH_BTN).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.INSTENCES_SEARCH_TF, 10)
            input_VALUE_tf = driver.find_element(By.CSS_SELECTOR, self.INSTENCES_SEARCH_TF)
            input_VALUE_tf.clear()
            input_VALUE_tf.send_keys(wfname)
                    
            
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.INSTENCES_WF_NAME, 10)    
            WFD = selenium_tools().getText(driver, By.CSS_SELECTOR, self.INSTENCES_WF_NAME) 
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.INSTENCES_STATE, 10)    
            STATE = selenium_tools().getText(driver, By.CSS_SELECTOR, self.INSTENCES_STATE)
#             if WFD == str(wfname) & STATE == "Completed":
            if WFD == str(wfname) and STATE == "Completed":
                print("Trigger WFD SUCCESSFULLY")
                driver.find_element(By.CSS_SELECTOR, self.INSTENCES_STATE).click()
#                 sleep(10)
#                 selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.INSTENCES_DETAIL_CLOSE_BTN,10)
                sleep(5)
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INSTENCES_DETAIL_CLOSE_BTN)))
                print("Found elemets")
#                 sleep(5)
                driver.find_element(By.CSS_SELECTOR, self.INSTENCES_DETAIL_CLOSE_BTN).click()
                print("clicked on elememts")
                
            else:
                driver.find_element(By.CSS_SELECTOR, self.INSTENCES_STATE).click()
                sleep(5)
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.INSTENCES_DETAIL_CLOSE_BTN)))
                print("Found elemets")
                driver.find_element(By.CSS_SELECTOR, self.INSTENCES_DETAIL_CLOSE_BTN).click()
                print("clicked on elememts")
                raise AssertionError("Failed! Trigger WFD failed")
            
        except:
            raise AssertionError("Failed TO CHECK WORKFLOW INSTENCES")
        

#################################################################################################################
    #Cleanup
    
    def open_new_tabs (self, driver, URL):
        
        print("open new tab")
        driver.execute_script("window.open('" +URL+ "');")
        driver.switch_to.window(driver.window_handles[1])
        
        
    
    def delete_wf(self,driver, wfname):
        print("start cleanup wf tab")  

#         driver.switch_to.window(driver.window_handles[0])
#         driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.WF_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.WF_TAB).click()
            driver.find_element(By.CSS_SELECTOR, self.REFRESH_WF_BTN).click()   
    #       sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.WF_TF, 10)
            input_wfname_tf = driver.find_element(By.CSS_SELECTOR, self.WF_TF)
            input_wfname_tf.clear()
            input_wfname_tf.send_keys(wfname)
    #             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.WF_CHECKBOX, 10)
            checkbox = driver.find_element(By.CSS_SELECTOR, self.WF_CHECKBOX)
            checkbox.click()
    #             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.UNDEPLOY_WF_BTN, 10)
            undeploy = driver.find_element(By.CSS_SELECTOR, self.UNDEPLOY_WF_BTN)
            undeploy.click()
    #             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.CONFIRM_UNDEPLOY_WF_BTN, 10)
            confirm_undeploy = driver.find_element(By.CSS_SELECTOR, self.CONFIRM_UNDEPLOY_WF_BTN)
            confirm_undeploy.click()
            sleep(2)
                
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG, 10)    
            a = selenium_tools().getText(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG) 
            print(str(a))
            if a != "Successfully undeployed 1 workflow(s).":
                
    #           if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_TOAST_MSG, 5):
                raise AssertionError("Failed! MESSAGE IS NOT SHOWN")
            else:
                print("MESSGE IS SHOWN CORRECTLY")
         
        except:
            raise AssertionError("Failed undeploy wf")
        
    def delete_workflow_darft(self,driver, wfname):
        
        print("start delete workflow draft")
        
#         driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.WF_DRAFT_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.WF_DRAFT_TAB).click()
            driver.find_element(By.CSS_SELECTOR, self.REFRESH_WF_DRAFT_BTN).click()   
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.WF_DARFT_TF, 10)
            input_wf_draft_tf = driver.find_element(By.CSS_SELECTOR, self.WF_DARFT_TF)
            input_wf_draft_tf.clear()
            input_wf_draft_tf.send_keys(wfname)
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.WF_DRAFT_CHECKBOX, 10)
            wf_draft_checkbox = driver.find_element(By.CSS_SELECTOR, self.WF_DRAFT_CHECKBOX)
            wf_draft_checkbox.click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.DELETE_WF_DRAFT_BTN, 10)
            undeploy = driver.find_element(By.CSS_SELECTOR, self.DELETE_WF_DRAFT_BTN)
            undeploy.click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.CONFIRM_DELETE_WF_DRAFT_BTN, 10)
            confirm_undeploy = driver.find_element(By.CSS_SELECTOR, self.CONFIRM_DELETE_WF_DRAFT_BTN)
            confirm_undeploy.click()
            sleep(2)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG, 10)    
            a = selenium_tools().getText(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG) 
            print(str(a))
            if a != "Successfully deleted 1 workflow draft(s).":
                
    #           if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_TOAST_MSG, 5):
                raise AssertionError("Failed! MESSAGE IS NOT SHOWN")
            else:
                print("MESSGE IS SHOWN CORRECTLY")
        
        except:
            raise AssertionError("Failed delete wf draft")
        
    

    def delete_routing_rule (self, driver, routing_name):
        print("start delete Routing Rule")
        driver.refresh()
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_TAB).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_REFRESH_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_REFRESH_BTN).click()   
            sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_SEARCH_TF, 10)
            input_WF_tf = driver.find_element(By.CSS_SELECTOR, self.ROUTING_SEARCH_TF)
            input_WF_tf.clear()
            input_WF_tf.send_keys(routing_name)
            sleep(2)
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_CHECKBOX, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_CHECKBOX).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_DELETE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_DELETE_BTN).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.ROUTING_DELETE_CONFIRM_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.ROUTING_DELETE_CONFIRM_BTN).click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG, 10)    
            a = selenium_tools().getText(driver, By.CSS_SELECTOR, self.UNDEPLOY_TOAST_MSG) 
            print(str(a))
            if a != "Successfully Deleted Routing Rule(s).":
                
    #           if selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.SAVE_TOAST_MSG, 5):
                raise AssertionError("Failed! MESSAGE IS NOT SHOWN")
            else:
                print("MESSGE IS SHOWN CORRECTLY")
            

        except:
            raise AssertionError("Failed to delete Routing Rule") 
            
              
    def delete_rules (self,driver, rulesetname):
        print("strat delete Rules")
         
#         driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        
        
        try:
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_TAB, 10)
            driver.find_element(By.CSS_SELECTOR, self.RULES_TAB).click()
             
            driver.find_element(By.CSS_SELECTOR, self.REFRESH_RULES_BTN).click()
             
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_TF, 10)
            input_RULES_tf = driver.find_element(By.CSS_SELECTOR, self.RULES_TF)
            input_RULES_tf.clear()
            input_RULES_tf.send_keys(rulesetname)      
             
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_CHECKBOX, 10)
            rules_checkbox = driver.find_element(By.CSS_SELECTOR, self.RULES_CHECKBOX)
            rules_checkbox.click()
#             sleep(2)
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.RULES_DELETE_BTN, 10)
            delete_rules = driver.find_element(By.CSS_SELECTOR, self.RULES_DELETE_BTN)
            delete_rules.click()
            
            selenium().wait_for_element_appear(driver, By.CSS_SELECTOR, self.OK_DELETE_BTN, 10)
            driver.find_element(By.CSS_SELECTOR, self.OK_DELETE_BTN).click()          
            
        except:
            raise AssertionError("Failed delete rules") 

                   
            
                  
        