
import subprocess, datetime, time, os, sys
from UTILITY.Function9611 import *

class PTI_9611():
    def __init__(self, ip = None, port = None):
        print("hello: " + str(ip) + str(port))
        self.tc_name = ' hello testcase name'
        self.ip = ip
        self.port = port


    def set_tc_name(self, tc_name):
        print(tc_name)
        self.tc_name = tc_name

    def pti_make_call(self, extension):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_make_call")
#             setHeadset(self.ip, "on")
            setSpeaker(self.ip, "on")
            sendNumber(self.ip, extension)
            sendKey(self.ip, "#")
            
            time.sleep(2)
             # assert(verifyPhoneStatus(self.ip, "SPKR_ON"))
            #logger.warn("pti_make_call to " + extension + " --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_make_call Failed" + '\n\n\n')

    def pti_end_call(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_end_call")
            if endCall(self.ip):
#                 logger.warn("pti_end_call --> Passed")
                return True
            raise AssertionError( "pti_end_call Failed" + '\n\n\n')
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError( "pti_end_call Failed" + '\n\n\n')

    def pti_answer_call(self):
        try:
#             logger.warn("Waiting incoming call")
            # time.sleep(10)
#             logger.info(self.tc_name + " --   starting process for command pti_answer_call")
            if answerCall(self.ip):
#                 logger.warn("pti_answer_call --> Passed")
                return True
            raise AssertionError( "pti_answer_call Failed" + '\n\n\n')
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError( "pti_answer_call Failed" + '\n\n\n')

    def pti_answer_call_with_headset(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_answer_call_with_headset")
            if answerCallWithHeadset(self.ip):
#                 logger.warn("pti_answer_call --> Passed")
                return True
            raise AssertionError("pti_answer_call_with_headset Failed" + '\n\n\n')
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_answer_call_with_headset Failed" + '\n\n\n')

    def pti_take_screen_shot(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_take_screen_shot")
            takeScreenShot(self.ip, self.tc_name)
#             logger.warn("pti_take_screen_shot --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError( "pti_take_screen_shot Failed" + '\n\n\n')

    def pti_press_key(self, key):
        try:
            print("IP " + self.ip)
            print("PORT " + self.port)
#             logger.info(self.tc_name + " --   starting process for command pti_press_key")
            sendKey(self.ip, key)
#             logger.warn("pti_press_key --> Passed")
            return True
        except:
            print("execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            #logger.error("execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError( "pti_press_key Failed" + '\n\n\n')

    def pti_log_out_H323(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_log_out_H323")
            logout_H323(self.ip)
#             logger.warn("pti_log_out_H323 --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError( "pti_log_out_H323 Failed" + '\n\n\n')

    def pti_log_out_SIP(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_log_out_SIP")
            logout_SIP(self.ip)
#             logger.warn("pti_log_out_SIP --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_log_out_SIP Failed" + '\n\n\n')

    def pti_log_in_H323(self, username, password):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_log_in_H323")
            login_H323(self.ip, username, password)
#             logger.warn("pti_log_in_H323 --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_log_in_H323 Failed" + '\n\n\n')

    def pti_log_in_SIP(self, username, password):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_log_in_SIP")
            login_SIP(self.ip, username, password)
#             logger.warn("pti_log_in_SIP --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_log_in_SIP Failed" + '\n\n\n')

    def pti_make_conference_call(self, bridge, code):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_make_conference_call")
            setHeadset(self.ip, "on")
            sendNumber(self.ip, bridge)
            time.sleep(5)
            sendNumber(self.ip, code + "#")
            time.sleep(5)
            assert(verifyPhoneStatus(self.ip, "lap5_g_on"))
#             logger.warn("pti_make_conference_call to bridge" + bridge + "with code " + code  + " --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError( "pti_make_conference_call Failed" + '\n\n\n')

    def pti_bridge_line_appearance(self, lineNumber):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_bridge_line_appearance")
            assert(bridgeLineAppearance(self.ip, lineNumber))
            setHeadset(self.ip, "on")
#             logger.warn("pti_bridge_line_appearance --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_bridge_line_appearance Failed" + '\n\n\n')

    def pti_end_conference(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_end_conference")
            endConference(self.ip)
#             logger.warn("pti_end_conference --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_end_conference Failed" + '\n\n\n')

    def pti_clean_up(self):
        try:
#             logger.info(self.tc_name + " --   starting process for command pti_clean_up")
            cleanUp(self.ip)
#             logger.warn("pti_clean_up --> Passed")
            return True
        except:
#             logger.error(
#                 "execute failed with exception :" + str(sys.exc_info()[0]) + " :: " + str(sys.exc_info()[1]))
            raise AssertionError("pti_clean_up Failed" + '\n\n\n')


