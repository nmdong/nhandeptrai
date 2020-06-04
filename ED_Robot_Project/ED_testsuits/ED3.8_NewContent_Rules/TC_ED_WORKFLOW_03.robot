
*** Settings *** 
Library    ../../apps/ED_webs/ED_keywords.py    WITH NAME    browser_03
Library    SSHLibrary.library.SSHLibrary  
Library    ../../JmetterLibrary/JMeterLib.py 
Library    ../../JmetterLibrary/JMeterClasses.py    

Resource    ../ED_testsuits_web/ED_Variables.robot
Resource    ../Robot_ED_Keywords/Robot_keywords.robot
        
Test Teardown    browser_03.Close Browser
# Test Teardown    browser_03.Clean Up TC And Close Browser    ${wfname}    ${wfname}

*** Variables ***
${wfname}    TC1728_WF8974_HTTP_Node_var
${locator}    D:\\ED\\TCs_Robot\\
${ruleset_name}    TC1728WF8974
${jmetterfile}    TC1728.jmx

*** Test Cases ***
Login user TC    
    Log To Console    ED3.8_WORKFLOW-8974_03 Add multiple conditions and treatment for a variable in Variables node for a ruleset then run HTTP WFD including IFTTT task    
        
    CheckBreezeVersion
  
    Log To Console    1. Use Chrome to access to ED consoles
    
    Log To Console    Launch new browser and go to admin page (https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html)
    browser_03.Open Browser    ${DESIGNER_URL}  
    Log To Console    Verify login ed Admin Page  
    browser_03.Verify Login Designer Page 
    Log To Console    Login user Admin Page
    browser_03.Login Designer Page   ${username_smgr}    ${password_smgr}
    browser_03.Verify Designer Page
    
   
    Log To Console    2. Design a HTTP WFD including IFTTT task using the created ruleset for the use case above (Use Make Call task to make call to calling/callee parties)    
    browser_03.Import Wf    ${locator}    ${wfname}
    sleep    2    
    browser_03.Save Wf    ${wfname}    ${ruleset_name}
    browser_03.Validate And Deploy Wf    ${wfname}
    sleep    1
            

    Log To Console    3. In Admin console, create a ruleset including multiple conditions (IF) in a rule, and make the treatment (THEN) for a variable in Variables node    
    Log To Console    Open new Tab (Admin console)
    browser_03.Open New Tab     ${ADMIN_URL}
    browser_03.Edit Rules http    ${ruleset_name}    ${EXTENSION1}    Yes    ${PROMPT}    ${CALLING_VARIABLE_HTTP}    
    Sleep    3    
    

    Log To Console    4. Use Jmeter to send a POST HTTP request to ED, that satisfies both conditions
    run_jmetter    ${jmetterfile} 
    Sleep    3    
    phoneA_answer_call
    Sleep    3    
    phoneB_answer_call
    Sleep    10   
    phoneA_end_call
    
    browser_03.Check Wf Instences    ${wfname}
    Log To Console    6. Check ED log and asm log    
     
    getLogGrepErr_ED
    # getLogGrepErr_SM
    

    Log To Console    Clean up TCs    
    browser_03.Clean Up TC And Close Browser    ${wfname}     
    

   