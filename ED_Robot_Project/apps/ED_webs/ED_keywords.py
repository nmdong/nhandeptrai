'''
Created on Apr 17, 2020

@author: GI-LAB


ED team is Engagement Designer team.


'''

import time
import sys
import os
from robot.libraries.BuiltIn import BuiltIn
# from robot.api import logger


from ultis.grid_manager.grid_driver_factory import grid_driver_factory
# from ultis.grid_manager.selenium_driver import selenium_driver



# from atda_web.pom.login_page import login_page
# from atda_web.pom.dash_board_page import dash_board_page
# from atda_web.pom.register_page import register_page

# from JMeterLib import JMeterLib

from ED_webs.pom.admin_console_page import admin_console_page
from ED_webs.pom.designer_console_page import designer_console_page
from ED_webs.pom.smgr_page import smgr_page

class ED_keywords(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """ Containing driver and all basic funciton.s

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    
    def adf(self):
        print("ddd")
        

    def __init__(self, ip_devices=None):
        """Example of docstring on the __init__ method.
 
        Examples:
            N/A
 
        Args:
            desired_capabilities: - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
            command_executor: - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.
 
        """
        print('*INFO:%d* Start function close_browser' % (time.time()*1000))
        CHROME = {'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
        if not ip_devices:
            command_executor='http://127.0.0.1:4444/wd/hub'
            command_executor_2='http://127.0.0.1:5555/wd/hub' #test
        BuiltIn().log_to_console('Init ATDA')
        self.desired_capabilities = CHROME
        self.command_executor = command_executor
        
        self.command_executor_2 = command_executor_2 #test
        
         
    def open_browser(self, url):
        """Launch web browser with ATDA server info
   
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
   
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
   
        Note:
            Do not include the `self` parameter in the ``Args`` section.
   
        Args:  
            url (str): Link to website
   
        """
#         BuiltIn().log_to_console('Launching browser: ' + self.desired_capabilities.get('browserName'),'')
        BuiltIn().log_to_console('Open Browser: '+str(self.desired_capabilities)+','+self.command_executor)
        self.driver = grid_driver_factory().create_driver(self.command_executor, self.desired_capabilities)
        BuiltIn().log_to_console('Open URL')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        
        
    def open_browser_2(self, url):
        """Launch web browser with ATDA server info
   
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
   
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
   
        Note:
            Do not include the `self` parameter in the ``Args`` section.
   
        Args:  
            url (str): Link to website
   
        """
#         BuiltIn().log_to_console('Launching browser: ' + self.desired_capabilities.get('browserName'),'')
        BuiltIn().log_to_console('Open Browser: '+str(self.desired_capabilities)+','+self.command_executor_2)
        self.driver = grid_driver_factory().create_driver(self.command_executor_2, self.desired_capabilities)
        BuiltIn().log_to_console('Open URL')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
     
    def close_browser(self):
        """Close web browser
  
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
  
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
  
        Note:
            Do not include the `self` parameter in the ``Args`` section.
  
        Args:  
            url (str): Link to website
  
        """
        print('*INFO:%d* Start function close_browser' % (time.time()*1000))
        self.driver.quit()
        print('*INFO:%d* close_browser successfully' % (time.time()*1000))
        

########################################################################################################################################################
    
    def verify_login_page(self):
        """verify login page
  
        The method may be checking login page.
        return: TRUE/FALSE
  
        ex: verify_login_page
        """
        print("start function login page")
        a = smgr_page().load_login_page(self.driver).__bool__()
        print(a)
        if smgr_page().load_login_page(self.driver):
            print("verify_login_page Pass ben KEYWORD")
        else:
            print("verify_login_page failed ben KEYWORD")
            raise AssertionError("verify_login_page failed")
        
    def login_user_page(self, userName, password):
        """login user
  
        The method may be login user.
        return: TRUE/FALSE
  
        ex: verify_login_page
        """
        print("Start function login user " + userName)
        smgr_page().input_smgr_username(self.driver, userName)
        smgr_page().input_smgr_password(self.driver, password)
        smgr_page().click_logon_button(self.driver)
        
    def verify_login_admin_page(self):
        print("start verifying login ed admin page")
        if admin_console_page().load_login_admin_page(self.driver):
            print("Admin login page is loaded successfully")
        else:
            raise AssertionError("Admin login Page is not loaded")
        
    def login_admin_page(self, admin_userName, admin_password):
        admin_console_page().input_admin_username(self.driver, admin_userName)
        admin_console_page().input_admin_password(self.driver, admin_password)
        admin_console_page().click_logon_button(self.driver)
        
    def verify_admin_page(self):
        print("start verify admin page after login successfully")
        if admin_console_page().load_admin_page(self.driver):
            print("Admin page is loaded successfully")
        else:
            print("verify ed admin page failed")
            raise AssertionError("Admin Page is not loaded")
########################################################################        
        
    def verify_login_designer_page(self):
        print("start verify designer login page")
        if designer_console_page().load_login_designer_page(self.driver):
            print("Designer login page is loaded successfully")
        else:
            raise AssertionError("Designer Login page is not loaded")
        
    def login_designer_page(self, designer_userName, designer_password):
        designer_console_page().input_designer_username(self.driver, designer_userName)
        designer_console_page().input_designer_password(self.driver, designer_password)
        designer_console_page().click_logon_button(self.driver)
        
    def verify_designer_page(self):
        print("start verify Designer page after login successfully")
        if designer_console_page().load_designer_page(self.driver):
            print("Designer page is loaded successfully")
        else:
            print("verify ed Designer page failed")
            raise AssertionError("Designer Page is not loaded")
        
#######################################################################################################

## Designer console webpage method
    def import_wf(self, locator, wfname ):
        print("start import wf")
        designer_console_page().import_wfd(self.driver, locator, wfname)
        
 
    def save_wf(self,wfname, ruleset_name):
        print("satrt save workflow")
        designer_console_page().input_ruleset_IFTTT_task(self.driver, ruleset_name)
        designer_console_page().save_wfd(self.driver,wfname)
        
    def save_as_wf(self):
        print("satrt save as workflow")
        designer_console_page().save_as_wfd(self.driver)
        
    def validate_and_deploy_wf(self, wfname):
        print("start validate and deploy wf")
        designer_console_page().validate_wfd(self.driver)
        designer_console_page().deploy_wfd(self.driver, wfname)
        
    def navigate_to_AdminConsole(self):
        designer_console_page().navigate_to_AdminConsole(self.driver)
        
        
        
        
#         
##########################################################################################################

## Admin console webpage method
    def open_new_tab(self,URL_admin ):
        admin_console_page().open_new_tabs(self.driver, URL_admin)
        
                
    def edit_rules_callintercept(self, ruleset_name, extension1,Yes_or_No, prompt,calling_or_called):
        admin_console_page().edit_rules_callintercept(self.driver, ruleset_name, extension1, Yes_or_No, prompt,calling_or_called)

        
    def edit_rules_http(self, ruleset_name, extension1,Yes_or_No, prompt, calling_or_called ):
        admin_console_page().edit_rules_http(self.driver, ruleset_name, extension1, Yes_or_No, prompt, calling_or_called)

    def switch_tab(self):
        #NOT use now
        designer_console_page().switch_tab(self.driver)
        
    def add_route_called_party(self, wfname, routing_name, PRIORITY, EXTENSION2):
        admin_console_page().add_route_called_party(self.driver, wfname, routing_name, PRIORITY, EXTENSION2)
        
    def add_route_calling_party(self, wfname, routing_name, PRIORITY, EXTENSION1):
        admin_console_page().add_route_calling_party(self.driver, wfname, routing_name, PRIORITY, EXTENSION1)
        
    def check_wf_instences(self,wfname):
        admin_console_page().check_wf_instences(self.driver, wfname)
        
    def delete_routing_rule(self,routing_name):   
        admin_console_page().delete_routing_rule(self.driver, routing_name)
        
    def clean_up_TC_And_Close_Browser (self, wfname):
#         designer_console_page().navigate_to_AdminConsole(self.driver)
        try:

            admin_console_page().delete_wf(self.driver, wfname)
            admin_console_page().delete_workflow_darft(self.driver, wfname)
            admin_console_page().delete_rules(self.driver, wfname)
            
#             self.close_browser()
            
        except:
         
            admin_console_page().delete_workflow_darft(self.driver, wfname)
            admin_console_page().delete_wf(self.driver, wfname)
            admin_console_page().delete_rules(self.driver, wfname)
 
#             self.close_browser()    
        
        
########################################################################################################################################################

        
        