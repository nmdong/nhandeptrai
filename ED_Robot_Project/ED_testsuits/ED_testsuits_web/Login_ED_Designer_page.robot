
*** Settings *** 
Library    ../../apps/ED_webs/ED_keywords.py    WITH NAME    browser_03
Resource    ED_Variables.robot

Test Teardown    browser_03.Close Browser
*** Variables ***
${url}    https://ed-smgr.hcm.com/network-login/
${url_1}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//index.html
${url_2}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html
${username_smgr}    admin 
${password_smgr}    2tdp22ler
${wfname}    TC1728_WF8974_v0
${locator}    D:\\ED\\

*** Test Cases ***
Login user TC
    Log To Console    Start Login user
    Log To Console    1. Launch new browser and go to admin page (https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html)
    browser_03.Open Browser    ${DESIGNER_URL}
    # Sleep    2    
    
    Log To Console    2. Verify login ed admin page.  
    browser_03.Verify Login Designer Page
    # Sleep    2  
    
    Log To Console    3. Login user.
    browser_03.Login Designer Page   ${username_smgr}    ${password_smgr}
    Sleep    2
    browser_03.Verify Designer Page
    Sleep    1    
    
    browser_03.Import Wf    ${locator}    ${wfname}
    sleep    2