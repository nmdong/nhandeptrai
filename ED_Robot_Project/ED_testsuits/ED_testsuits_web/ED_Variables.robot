*** Variables ***

# Define browsers
${CHROME}    chrome
${FIREFOX}   firefox
${EDGE}      edge
${IE}        internet explorer
${SAFARI}    safari

#Platforms
${CAP_WINDOWS}    platform:WINDOWS
${CAP_MAC}        platform:MAC

# Browsers capability
${CAP_CHROME}    browserName:chrome
${CAP_FIREFOX}   browserName:firefox
${CAP_EDGE}      browserName:MicrosoftEdge
${CAP_SAFARI}    browserName:safari
${CAP_IE}        browserName:internet explorer

# Tested web page
${WEB_URL}    https://ed-smgr.hcm.com/securityserver/UI/Login?goto=https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//index.html
${ADMIN_PAGE}    Avaya Engagement Designer Administration Console
${SMGR_URL}    https://ed-smgr.hcm.com/network-login/
${ADMIN_URL}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html
${DESIGNER_URL}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//index.html
${DIFFTOOL_URL}    https://ed-smgr.hcm.com/securityserver/UI/Login?goto=https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//diff.html


# Selenium Grid hub - where the test send to
${HUB_URL}    http://100.20.43.158:4444/wd/hub

# Page title
${HOME_PAGE_TITLE}    Welcome: Mercury Tours

#LOGIN SMGR
${USERNAME}    xpath://*[@id="IDToken1"]
${PASSWORD}    xpath://*[@id="IDToken2"]

#User Info SMGR
${username_smgr}    admin 
${password_smgr}    2tdp22ler

#IMPORT TESTCASE
${IMPORTWF_BUTTON}   xpath=/html/body/div[15]/div/div[1]/button[1]
${BROWSE_BUTON}    xpath=//*[@id="importwfdfile"]
${FILE_PATH}    D:\\ED\\
#${IMPORT_BUTTON}    xpath=/html/body/div[36]/div[3]/div/button[2]/span
${IMPORT_BUTTON}    xpath=//*[@id="ext-gen16"]/div[37]/div[3]/div/button[2]



#SAVE WF
${SAVEWF_BUTTON}    xpath=//*[@id='narWorkflowFileNameImg']
${SAVEWF_BUTTON1}    xpath=//*[@id="narWfsavebox"]/div/div[4]/label
${SAVEWF_NAME}       xpath://*[@id="saveWfdWorkflowName"]
${SAVEWF_FOLDER}    xpath://*[@id='AutoTest_anchor']
${SAVEWF_SAVE}    xpath=//*[@id="ext-gen16"]/div[38]/div[3]/div/button[3]/span

${SAVEWF_DIFFTOOL_FOLDER}   xpath=//*[@id="DiffToolRobot_anchor"]

#DEPLOYWF
${DEPLOY_BUTTON}    xpath=/html/body/div[1]/div/div[1]/div/div/div[2]/button[2]
${DEPLOYWF}      xpath=//div[39]/div[3]/div/button[2]/span
${JMeter2_path}        D:/Robot/apache-jmeter-2.13/bin/jmeter.bat
${JMeter_path}    D:/ED/apache-jmeter-2.13/bin/jmeter.bat
${JMeter_script_1thread1loop_path}  D:/ED/JmetterFile
${JMeter_log01_path}    ED/JmetterLibrary/JMeter_test_files/jmeterTest1Thread1Loop_log01.jtl

#SSH breeze
${SSHSERVER}    avaya-breeze-06
${DATE}        date +"%Y-%m-%d %H:%M:%S"
${GET_ED_lOG}    tail -n 1250 /var/log/Avaya/services/EngagementDesigner/EngagementDesigner.log
${GET_SM_LOG}    tail -n 8 /var/log/Avaya/sm/asm.log | grep "ERROR "
${GET_ED_lOG_2}    tailf /var/log/Avaya/services/EngagementDesigner/EngagementDesigner.log | grep "ERROR "

${ERROR_ED}    EngagementDesigner ERROR - EngagementDesigner
${ERROR_SM}    ERROR 
${VERSIONSYSTEM}    swversion
#ADMIN CONSOLE
${ADMIN_PAGE_CONSOLE}   xpath=/html/body/div[1]/div/div[1]/div/div/div[2]/button[3]

#ROUTING
${ROUTING}               xpath://*[@id="routingLi"]/a

${CREAT_BUTTON}          xpath://*[@id="createRoutingRule"]
#${SELECT_EVENT_BUTTON}      xpath:/html/body/div[13]/div/div/div[2]/div/div[1]/div/div[1]/button/span[1]
${SELECT_EVENT_BUTTON}     xpath=//button[@data-id="routingevents"]
${CALLED_PARTY_TYPE}        xpath=//*[@id='rulesPanelHeading']/div[1]/div/ul/li[13]/a
${SELEC_WF}               xpath=//button[@data-id="routingworkflows"]
${WF_NAME_INPUT}                xpath=//*[@id="rulesPanelHeading"]/div[2]/div/div/input
${ROUTING_WFNAME}       xpath=//*[@id="rulesPanelHeading"]/div[2]/div/ul/li[1]/a/span[1]
${ROUTING_NAME}         xpath=//*[@id="ruleName"]
${ADDRULES}             xpath=//*[@id="addRuleOption"]
${SELEC_ATTRIBUTE}      xpath=//button[@data-id="atrdrop1"]
${CALLED_TYPE}          xpath=/html/body/div[51]/div/ul/li[7]/a/span[1]
${SELECT_FUNCTION}      xpath=//*[@id="rulesRow1"]/td/div[2]/button
${VALUE_BOX}            xpath=//*[@id="valuebox1"]
${FUNCTION}             xpath=/html/body/div[52]/div/div/input
${ENGAGEMENTDESIGNERBUTTON}     xpath=//*[@id="engDesignerLnk"]


#CLUSTER ADMINISTRATION
${DOMAINSEARCH}             xpath=//*[@id="domainsearch"]/span/span/span
${BREEZE_ELEMENTS}      xpath=/html/body/div[1]/div/div/div/div/div[1]/span/div/div[3]/div/div[2]/a/span[1]
${CLUSTER_ELEMENTS}      xpath=//li[2]/span[2]/span
${CLUSTER_URL}              xpath=//*[@id="clusterDashboardTable_core_table_content"]/tbody/tr[4]/td[17]/span
${VISIABLE}                 xpath=//iframe[contains(@id,'iframe0')]
${VISIABLE1}                xpath=//*[@id="clusterDashboardTable:2:selectTarget"]

#ENGAGEMENTDESIGNER
${MEDIA COMMUNICATIONS}     xpath=//*[@id="ext-gen260"]
${PLAY AND COLLECT TASK}    xpath=//*[@id="ext-gen261"]/ul/li[1]/div/div/img
${EDCANVAS}                   xpath=//*[@id="ext-gen216"]
${EDSETTINGBUTTON}            xpath=//*[@id="narsilverbar"]/div/div[3]/span[12]

#ADMINCONSOLE
${ENGAGEMENTDESIGNERBUTTON}     xpath=//*[@id="engDesignerLnk"]

#USERTASKPORTAL
${USERTASKPORTAL}          xpath=//*[@id="userTaskPortalLnk"]

#DIFFTOOL
${DIFFTOOLBUTTON}             xpath=//*[@id="narsettingBox"]/div/div[1]/label
${LEFTDIFFTOL}                xpath=//*[@id="leftfilechooser"]
${LOADLEFTDIFFTOOL}           xpath=//*[@id="openDraftLeft"]/label
${DIFFTOOLSEARCH}               xpath=//*[@id="searchWorkflow"]
${DIFFTOOLSEARCH2}               xpath=//*[@id="searchWfd"]
${DIFFTOOLNAME1}                xpath=//*[@id="Difftool1_anchor"]

${RIGHTDIFFTOL}                xpath=//*[@id="rightfilechooser"]
${LOADRIGHTDIFFTOOL}           xpath=//*[@id="openDraftRight"]/label
${CLICK_DIFFTOOL_FOLDER}        xpath=//*[@id="DiffToolRobot"]/i
${DIFFTOOLSEARCH}               xpath=//*[@id="searchWorkflow"]
${DIFFTOOLNAME2}                xpath=//*[@id="Difftool2_anchor"]
${DIFFTOOLOPEN}                 xpath=/html/body/div[15]/div[3]/div/button[2]
#${DIFFTOOLCANCLE}               xpath=/html/body/div[15]/div[3]/div/button[1]
${DIFFTOOLDEPLOYEDWORKFLOW}         xpath=//*[@id="ui-id-7"]
${DIFFTOOLWORKFLOWSEARCH}            xpath=//*[@id="wffilenamesearchstr"]

${DIFFTOOLLEFTLOCAL}        xpath=//*[@id="xmlfile"]
${DIFFTOOLRIGHTLOCAL}       xpath=//*[@id="xmlfile2"]
${DIFFTOOL_FILE_PATH}       D:\\ED\\DiffTool\\
${SHOWDIFF}                 xpath=/html/body/div[2]/div[2]/button
${MODIFY}                   xpath=//*[@id="leftTable"]/tr[1]/td[3]/span[1]
${BOTH_THE_SAME}            xpath=/html/body/div[15]

${LEFTLOCALFILEIMPORT}              xpath=//*[@id="fileLeftChooserBox"]/div[4]/label


${EXTENSION1}    2012061
${EXTENSION2}    2012062
${PROMPT}    Hello Mr Khanh mr Khanh Mr Khanh Mr Khanh and Mr Nhan handsome boy to E D S V VIP customer wow wow wow wow
${PRIORITY_1}    1
${CALLING_VARIABLE_HTTP}    StartSchema.CallingParty
${CALLED_VARIABLE_HTTP}     StartSchema.CalledParty
${CALLING_VARIABLE_CALLINTERCEPT}    StartSchema.callingParty.handle
${CALLED_VARIABLE_CALLINTERCEPT}    StartSchema.calledParty.handle

${locator}    D:\\ED\\

${url}    https://ed-smgr.hcm.com/network-login/
${url_1}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//index.html
${url_2}    https://avaya-breeze-06-sec.hcm.com/services/EngagementDesigner//admin.html
