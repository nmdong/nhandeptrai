
import subprocess, datetime, time, os

# Replace path for each location of test suite (.robot)

directoryScreenShotPath = os.getcwd()\
                .replace('TESTS\sanity_suite', 'Tools\PTI_ScreenShot')\
                .replace('TESTS\Demo_TCs', 'Tools\PTI_ScreenShot')
                
path = str(os.getcwd()).split('SOCKETBOT')
delim = "/"
if not str(os.name) == "nt":
    delim = "/"
else:
    delim = "\\"
pti_path = 'C:\\Users\\GI-LAB\\ED-WorkSpace\\ED_Robot_Project\\apps\\Tools\\'

keyMap = {
  "0": "0x100",
  "1": "0x101",
  "2": "0x102",
  "3": "0x103",
  "4": "0x104",
  "5": "0x105",
  "6": "0x106",
  "7": "0x107",
  "8": "0x108",
  "9": "0x109",
  "star": "0x10A",
  "*": "0x10A",
  "hash": "0x10B",
  "#": "0x10B",

  "softKey0": "0x600",
  "softKey1": "0x601",
  "softKey2": "0x602",
  "softKey3": "0x603",

  "phone": "0x405",

  "menu": "0x408",
  "message": "0x407",
  "addressBook": "0x409",
  "callLog": "0x40A",
  "forward": "0x40B",
  "home": "0x408",
  "options": "0",
  "hold": "0",
  "transfer": "0",
  "conference": "0",
  "redial": "0",
  "drop": "0",
  "pageLeft": "0",
  "pageRight": "0",

  "headset": "0x404",
  "headsetOn": "0x462",
  "headsetOff": "0x463",
  "speaker": "0x400",
  "mute": "0x401",
  "volumeUp": "0x402",
  "volumeDown": "0x403",

  "lineAppearance1": "0x200",
  "lineAppearance2": "0x201",
  "lineAppearance3": "0x202",
  "lineAppearance4": "0x203",
  "lineAppearance5": "0x204",
  "lineAppearance6": "0x205",

  "navUp": "0x502",
  "navDown": "0x503",
  "navLeft": "0x500",
  "navRight": "0x501",
  "navUpPage": "0x504",
  "navDownPage": "0x505",
  "navOk": "0x506"
}


# Define keyword
def sendKey(phoneIP, key):
    print("start sendkey")
    pti_send = subprocess.Popen(pti_path + "pti.exe -i "+ phoneIP + " -Z 200 -k " + keyMap[key], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = pti_send.stdout.readlines()
    print(output)
    print("Send key " + str(key))
    time.sleep(1)

def ansewerXY(phoneIP):
  pti_send = subprocess.Popen(pti_path + "pti -i " + phoneIP + " -t " + " 100 50 ", stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

def sendKeyWithLoopNumber(phoneIP, key, loopNumber):
  for x in range(loopNumber):
    pti_send = subprocess.Popen(pti_path + "pti -i " + phoneIP + " -Z 200 -k " + keyMap[key], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#     logger.info("Send key " + str(key))
    time.sleep(1)

# Send number

def sendNumber(phoneIP, number):
  hexString = ""
  for character in number:
    out = keyMap[character]
    hexString = hexString + " " + out
#   logger.info("send number: " + hexString)
  pti_send = subprocess.Popen(pti_path + "pti -i " + phoneIP + " -Z 200 -k " + hexString, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  time.sleep(2)

# Set headset

def setHeadset(phoneIP, setting):
  if setting == "on":
#     logger.info("Set headset on")
    if verifyPhoneStatus(phoneIP, "heds_off"):
      sendKey(phoneIP, "headset")
  else:
#     logger.info("Set headset off")
    if verifyPhoneStatus(phoneIP, "HEDS_ON"):
      sendKey(phoneIP, "headset")

# Set speaker

def setSpeaker(phoneIP, setting):
  if setting == "on":
#     logger.info("Set speaker on")
    if verifyPhoneStatus(phoneIP, "spkr_off"):
      sendKey(phoneIP, "speaker")
  else:
#     logger.info("Set speaker off")
    if verifyPhoneStatus(phoneIP, "spkr_on"):
      sendKey(phoneIP, "speaker")

# Verify Phone status

def verifyPhoneStatus(phoneIP, status) -> bool:
#   logger.info("Verify " + status)
  pti_get_log = subprocess.Popen(pti_path + "pti -i " + phoneIP + " -A", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  output = pti_get_log.stdout.readlines()
  for target_list in output:
    #out = str(target_list).replace("b'", "").replace("\\r\\n'", "").lower()
    out = str(target_list)
   # out = output
    if status in out:
      return True
  return False

# Verify Idle

def verifyIdle(phoneIP):

  assert (not verifyPhoneStatus(phoneIP, "HEDS_ON") and not verifyPhoneStatus(phoneIP, "SPKR_ON") and not verifyPhoneStatus(phoneIP, "RING_FL"))

# Verify active call

def verifyActiveCall(phoneIP):
  assert (verifyPhoneStatus(phoneIP, "HEDS_ON") or verifyPhoneStatus(phoneIP, "SPKR_ON") or verifyPhoneStatus(phoneIP, "RING_FL"))

# End call

def endCall(phoneIP) -> bool:
  if verifyPhoneStatus(phoneIP, "HEDS_ON") or verifyPhoneStatus(phoneIP, "SPKR_ON"):
#     logger.info("There is activate call")
    if verifyPhoneStatus(phoneIP, "HEDS_ON"):
      sendKey(phoneIP, "headset")
    if verifyPhoneStatus(phoneIP, "SPKR_ON"):
      sendKey(phoneIP, "speaker")
    time.sleep(2)
    verifyIdle(phoneIP)
    return True
  else:
#     logger.info("There is no activate call")
    return False

# Answer call without headset

def answerCall(phoneIP) -> bool:
  if verifyPhoneStatus(phoneIP, "RING_FL"):
#     logger.info("There is incoming call")
    #ansewerXY(phoneIP)
    sendKey(phoneIP,"speaker")
    time.sleep(2)
    verifyActiveCall(phoneIP)
#     logger.info("Answer call successfully")
    return True
  else:
#     logger.info("There is no incoming call")
    return False

# Answer call with headset

def answerCallWithHeadset(phoneIP) -> bool:
  if verifyPhoneStatus(phoneIP, "lap5_g_fl"):
#     logger.info("There is incoming call")
    sendKey(phoneIP, "softKey0")
    time.sleep(2)
    setHeadset(phoneIP, "on")
    verifyActiveCall(phoneIP)
#     logger.info("Answer call successfully")
    return True
  else:
#     logger.info("There is no incoming call")
    return False

# Capture Screen

def takeScreenShot(phoneIP, tcName):
  timeString = str(datetime.datetime.now()).replace(':', '-').replace(' ', '--')
  pti_send = subprocess.Popen(pti_path + "pti -i " + phoneIP + " -S " + tcName + "_" + timeString, cwd=directoryScreenShotPath)
#   logger.info("Screen shot was saved at: " + directoryScreenShotPath)

# Log out

def logout_H323(phoneIP):
  sendKey(phoneIP, "menu")
  sendKeyWithLoopNumber(phoneIP, "navDown", 3)
  sendKeyWithLoopNumber(phoneIP, "softKey0", 2)
  sendKeyWithLoopNumber(phoneIP, "softKey1", 7)
  assert(verifyPhoneStatus(phoneIP, "lap5_r_off"))
#   logger.info("Log out on H323 phone successfully")
def logout_SIP(phoneIP):
  sendKey(phoneIP, "menu")
  sendKeyWithLoopNumber(phoneIP, "navDown", 5)
  sendKeyWithLoopNumber(phoneIP, "softKey0", 2)
  time.sleep(10)
  assert(verifyPhoneStatus(phoneIP, "lap5_r_off"))
#   logger.info("Log out on SIP phone successfully")

# Log in

def login_H323(phoneIP, username, password):
  sendKeyWithLoopNumber(phoneIP, "softKey0", 3)
  sendKey(phoneIP, "softKey1")
  sendNumber(phoneIP, username)
  time.sleep(1)
  sendKey(phoneIP, "navOk")
  sendNumber(phoneIP, password)
  sendKey(phoneIP, "navOk")
  time.sleep(5)
  assert (verifyPhoneStatus(phoneIP, "lap5_r_on"))
#   logger.info("Log in on H323 phone successfully")
def login_SIP(phoneIP, username, password):
  sendNumber(phoneIP, username)
  time.sleep(1)
  sendKey(phoneIP, "navOk")
  sendNumber(phoneIP, password)
  sendKey(phoneIP, "navOk")
  time.sleep(5)
  assert (verifyPhoneStatus(phoneIP, "lap5_r_on"))
#   logger.info("Log in on SIP phone successfully")

# Bridge line appearance

def bridgeLineAppearance(phoneIP, lineNumber) -> bool:
  sendKeyWithLoopNumber(phoneIP, "navUp", int(lineNumber))
  assert (verifyPhoneStatus(phoneIP, "lap5_r_on") and verifyPhoneStatus(phoneIP, "lap5_g_on"))
  sendKey(phoneIP, "navOk")
  if verifyPhoneStatus(phoneIP, "lap5_g_bf"):
#     logger.info("Cannot bridge to line ...")
    return False
#   logger.info("Bridge to line successfully ...")
  return True

# End conference

def endConference(phoneIP):
  assert (verifyPhoneStatus(phoneIP, "lap5_r_on") and verifyPhoneStatus(phoneIP, "lap5_g_on"))
  sendKey(phoneIP, "navOk")
  sendKey(phoneIP, "softKey3")
  setHeadset(phoneIP, "off")
  setSpeaker(phoneIP, "off")
  verifyIdle(phoneIP)
#   logger.info("End conference successfully")

# Clean up

def cleanUp(phoneIP):
  try:
      if verifyPhoneStatus(phoneIP, "SPKR_ON"):
        sendKey(phoneIP, "speaker")
      if verifyPhoneStatus(phoneIP, "HEDS_ON"):
        sendKey(phoneIP, "headset")
      if verifyPhoneStatus(phoneIP, "RING_FL"):
        sendKey(phoneIP, "navUp")
        sendKey(phoneIP, "navOk")
        sendKey(phoneIP, "softKey3")
      if verifyPhoneStatus(phoneIP, "SPKR_ON"):
        sendKey(phoneIP, "speaker")
  except:
      assert (verifyPhoneStatus(phoneIP, "ring_off"))
#       logger.info("Clean up successfully")


