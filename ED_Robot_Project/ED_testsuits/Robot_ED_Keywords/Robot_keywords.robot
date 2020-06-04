*** Settings ***


Library    SSHLibrary.library.SSHLibrary
Library    SSHLibrary.library    

Library   ../../JmetterLibrary/JMeterLib.py 
Library   ../../JmetterLibrary/JMeterClasses.py  
Library   ../../apps/ED_webs/PTI_9611.py    100.20.43.141	5060	WITH NAME	sipPhoneA
Library   ../../apps/ED_webs/PTI_9611.py    100.20.43.142	5060	WITH NAME	sipPhoneB

Resource   ../ED_testsuits_web/ED_Variables.robot


*** Keywords ***

Close_ssh_connection
    Close Connection
    Close All Connections    

getLogGrepErr_taif
    Log To Console    getLogGrepErr_taif
    Open Connection    100.20.128.60    port=22   
    Log To Console    start login  
    Login    cust    2tdp22ler    delay=0.5
    Log To Console    execute command
    ${output1}=    Execute Command    	${GET_ED_lOG_2}
        
    Log To Console    Check ED Log
    Should Not Contain    ${output1}    ${ERROR_ED}
    Log to console  Close Session
    # Close Connection
    # Close All Connections

getLogGrepErr_ED
    Log To Console    getLogGrepErr
    Open Connection    100.20.128.60    port=22   
    Log To Console    start login  
    Login    cust    2tdp22ler    delay=0.5
    
    Log To Console    execute command
    ${output2}=    Execute Command    	${GET_ED_lOG}  
        
    Log To Console    Check ED Log
    Should Not Contain    ${output2}    ${ERROR_ED}
    
    Log to console  Close Session
    Close Connection
    Close All Connections
    
getLogGrepErr_SM
    Log To Console    getLogGrepErr
    Open Connection    100.20.128.60    port=22   
    Log To Console    start login  
    Login    cust    2tdp22ler    delay=0.5
    
    Log To Console    execute command
    ${output3}=    Execute Command    	${GET_SM_LOG}      
    Log To Console    Check SM Log
    Should Not Contain    ${output3}    ${ERROR_SM}

    Log to console  Close Session
    Close Connection
    Close All Connections
    
    
    
CheckBreezeVersion
    Log To Console    Start ssh to server    
    Open Connection    100.20.128.60    port=22
    Log To Console    start login    
    Login    cust    2tdp22ler    delay=0.5
    
    Log To Console    execute command
    ${output} =  Execute Command    swversion
    # Log To Console    ${output}     
    Log to console  Close Session
    Close Connection 
    Close All Connections
    
    
run_jmetter
    [Arguments]    ${jmetterfile}
    Run Jmeter    ${JMeter_path}    ${JMeter_script_1thread1loop_path}/${jmetterfile}    ${JMeter_log01_path} 
    
phoneA_make_call
    [Arguments]    ${extension1}
    sipPhoneA.Pti Make Call    ${extension1}
    Sleep    3    
    
phoneB_make_call
    [Arguments]    ${extension2}
    sipPhoneB.Pti Make Call    ${extension2}
    Sleep    3   
    
phoneA_answer_call
    sipPhoneA.Pti Answer Call
    Sleep    3 
    
phoneB_answer_call
    sipPhoneB.Pti Answer Call
    Sleep    3 
    
phoneA_end_call
    sipPhoneA.Pti End Call
    Sleep    3 
    
phoneB_end_call
    sipPhoneB.Pti End Call
    Sleep    3 
       
test_A_call_B
    sipPhoneA.Set Tc Name    Tc_Name_ne
    
    sipPhoneA.Pti Make Call    2012062
    # sipPhoneA.Pti Press Key    speaker
    
    
    