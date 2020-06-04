from SETUP.Pune.TB2 import Data
from UTILITY.CreateUser import Host





# Define host structures here
# format is as follows:-
# <HostName> = Host(<host_ip_address>,<host_port>,<host_playID>,<host_recordID>)

#HardPhones
HOST_9611_H323_01 = Host(Data.ip_hard_phone_H323_9611_01, None, None, None,Data.speechVerification,Data.mobileSpeechVerification)
HOST_9611_H323_02 = Host(Data.ip_hard_phone_H323_9611_02, None, None, None,Data.speechVerification,Data.mobileSpeechVerification)

HOST_9611_SIP_01 = Host(Data.ip_hard_phone_SIP_9611_01, None, None, None,Data.speechVerification,Data.mobileSpeechVerification)
HOST_9611_SIP_02 = Host(Data.ip_hard_phone_SIP_9611_02, None, None, None,Data.speechVerification,Data.mobileSpeechVerification)
