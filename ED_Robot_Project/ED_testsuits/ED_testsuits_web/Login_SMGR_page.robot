
*** Settings *** 
Library    ../../apps/ED_webs/ED_keywords.py    WITH NAME    browser_02
Resource    ED_Variables.robot

Test Teardown    browser_02.Close Browser
*** Variables ***
${url}    https://ed-smgr.hcm.com/network-login/
${url_1}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//index.html
${url_2}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html
${username_smgr}    admin 
${password_smgr}    2tdp22ler

*** Test Cases ***
Login user TC
    Log To Console    Start Login user
    Log To Console    1. Launch new browser and go to address(http://100.20.128.35/network-login/)
    browser_02.Open Browser    ${SMGR_URL}
    Sleep    2    
    
    Log To Console    2. Verify login page.  
    browser_02.Verify Login Page
    Sleep   1
    browser_02.Login User Page    ${username_smgr}    ${password_smgr}
    Sleep    4    
    
    Log To Console    3. Login user.
    