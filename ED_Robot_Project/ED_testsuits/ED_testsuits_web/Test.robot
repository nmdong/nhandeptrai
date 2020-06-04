
*** Settings *** 
Library    ../../apps/ED_webs/ED_keywords.py    WITH NAME    browser_03

Library    SSHLibrary.library.SSHLibrary  

Library    ../../JmetterLibrary/JMeterLib.py 
Library    ../../JmetterLibrary/JMeterClasses.py    



Resource    ED_Variables.robot
Resource    ../Robot_ED_Keywords/Robot_keywords.robot

           
Test Teardown    browser_03.Close Browser
*** Variables ***
${url}    https://ed-smgr.hcm.com/network-login/
${url_1}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//index.html
${url_2}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html
${username_smgr}    admin 
${password_smgr}    2tdp22ler
# ${wfname}    TC1728_WF8974_v1_test
${wfname}    TC175W01
${locator}    D:\\ED\\
${ruleset_name}    TC175W01

# ${GET_ED_lOG}    	tail -1200 /var/log/Avaya/services/EngagementDesigner/EngagementDesigner.log | grep "ERROR "
# ${ERROR}    EngagementDesigner ERROR - EngagementDesigner

${jmetterfile}    TC175.jmx


*** Test Cases ***
Login user TC
    
    # test_A_call_B
    
    CheckBreezeVersion
    sleep    1
    
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
    browser_03.Save Wf    ${wfname}    ${ruleset_name}
    browser_03.Validate And Deploy Wf    ${wfname}
    sleep    1
            
    # run_jmetter    ${jmetterfile}
    phoneA_make_call    ${EXTENSION2}
    phoneB_answer_call
    Sleep    5    
    phoneA_end_call
    
    Log To Console    4.Open new Tab (Admin console)
    browser_03.Open New Tab     ${ADMIN_URL}
    # browser_03.Edit Rules    ${ruleset_name}    ${EXTENSION1}    Yes
    
    
    
    
    # getLogGrepErr
    
    Log To Console    Clean up TCs    
    # browser_03.Clean Up TC    ${wfname}     
    
    

    

    

    
        
    
     
   