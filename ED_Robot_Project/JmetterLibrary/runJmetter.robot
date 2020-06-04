#*** Settings ***
#Library           JMeterLib.py
#Library           Collections
#
#
#*** Variables ***
#${JMeter2_path}    D:/Robot/apache-jmeter-2.13/bin/jmeter.bat
#${JMeter3_path}    D:/programy/apache-jmeter-3.3/bin/jmeter.bat
#${JMeter_script_1thread1loop_path}    D:/ED/JmetterFile/TC175.jmx
#${JMeter_log01_path}    ED/JmetterLibrary/JMeter_test_files/jmeterTest1Thread1Loop_log01.jtl
#
#
#*** Test Cases ***
#jmeter2_tc1_justRunJMeter
##    [Arguments]    ${jmetterfile}
##    runjmeter    ${JMeter2_path}    ${JMeter_script_1thread1loop_path}    ${JMeter_log01_path}
#    runjmeter    ${JMeter2_path}    ${JMeter_script_1thread1loop_path}    ${JMeter_log01_path}
#
##jmeter2_tc2_analyseAndConvertExistingJtlLog
##    ${result}     runJmeterAnalyseJtlConvert    ${JMeter_log01_path}
##    log    ${result}
##    : FOR    ${ELEMENT}    IN    @{result}
##    \    log dictionary    ${ELEMENT}
#
