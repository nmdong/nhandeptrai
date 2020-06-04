# *** Settings ***
# # Do all the necessary imports here.
# # Library  ExtensionsForRobot.py
# Library  Logger.py
# Library  String
# Library  OperatingSystem
# # make sure that these variables are properly imported from correct test bed
# # before you begin execution.
# Variables  ../SETUP/Pune/TB2/Data.py
# Variables  ../SETUP/Pune/TB2/HostData.py
# # EQUINOX CLIENTS


# #HARDPHONES
# Library  CLIENTS.SOCKET_IMPLEMENTED.PTI_9611  ${host 9611 h323 01}  WITH NAME  h323PhoneA
# Library  CLIENTS.SOCKET_IMPLEMENTED.PTI_9611  ${host 9611 h323 02}  WITH NAME  h323PhoneB

# Library  CLIENTS.SOCKET_IMPLEMENTED.PTI_9611  ${host 9611 h323 01}  WITH NAME  sipPhoneA
# Library  CLIENTS.SOCKET_IMPLEMENTED.PTI_9611  ${host 9611 h323 02}  WITH NAME  sipPhoneB


# *** Keywords ***
# set tc name
    # [Arguments]  ${tc_name}
    # # call this function in the begining of each TC for setting TC Name in the client libraries
    # # this way the log file will contain the TC Name.
    # h323PhoneA.set tc name  ${tc_name}
    # h323PhoneB.set tc name  ${tc_name}

# Execute Command
    # [Arguments]  @{args}
    # log to console  command sent is @{args}
    # log to logfile  command sent is @{args}
    # ${res} =  run keyword  @{args}
    # log to console  result obtained for '@{args}' is '${res}'
    # log to logfile  result obtained for '@{args}' is '${res}'
    # should be true  ${res}

# Execute_Test_Case
    # [Arguments]    ${tc_name}
    # log to console  Executing  ${tc_name}
    # ${result}=  run keyword  ${tc_name}
    # should be true  ${result}  True


# Execute CleanUp
    # [Arguments]  ${tc_name}  ${tc_result}  @{args}
    # run keyword if  ${tc_result} == 'FAIL'  @{args}
    # run keyword if  ${tc_result} == True  log to logfile  ${tc_name} PASSED  info
    # run keyword if  ${tc_result} == 'FAIL'  log to logfile  ${tc_name} FAILED info


# Log to logfile
    # [Arguments]  @{args}
    # run keyword  log to execution log file  @{args}

# Log to sumfile
    # [Arguments]  @{args}
     # run keyword  log to sum log file  @{args}


# clear log file
    # run keyword  clear log file contents

# instruction for future
    # [Arguments]  @{args}
    # log to console  Instruction From Previous Execution: @{args}
    # log to logfile  Instruction From Previous Execution: @{args}

# Try and Fail
    # [Arguments]  @{args}
    # log to console  command sent is @{args}
    # log to logfile  command sent is @{args}
    # ${res} =  run keyword and ignore error   @{args}
    # log to console  result obtained for '@{args}' is '${res}'
    # log to logfile  result obtained for '@{args}' is '${res}'
    # run keyword if  ${res} == True  FAIL ' @{args} ' failed in try block


# Try and Continue
    # [Arguments]  @{args}
    # log to console  command sent is @{args}
    # log to logfile  command sent is @{args}
    # ${res} =  run keyword and ignore error    @{args}
    # log to console  result obtained for '@{args}' is '${res}'
    # log to logfile  result obtained for '@{args}' is '${res}'