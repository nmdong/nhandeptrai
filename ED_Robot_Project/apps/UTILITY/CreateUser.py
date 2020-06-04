import os
from UTILITY.Function_Map import find_userdata_vars_required_in_lib
from UTILITY import Logger

logger = Logger.get_logger(__name__)

class User:
    def __init__(self,username,Data,isTMA=None,userpool_file_path=None):
        self.userdata = {}
        userdata_file_reader = ''
        if userpool_file_path:
            userdata_file_reader = open(str(userpool_file_path), 'r')
        else:
            # as userdata file path is not specified, use users from default user_pool
            cwd = os.getcwd()
            path = str(cwd).split('SOCKETBOT')
            if not isTMA:
                userdata_file_reader = open(path[0] + 'SOCKETBOT\SETUP\Pune\\USER_POOL.txt', 'r')
            else:
                userdata_file_reader = open(path[0] + 'SOCKETBOT\SETUP\TMA\\USER_POOL.txt', 'r')

        line = userdata_file_reader.readline()
        user_found = False
        userdata_str = ''
        while line:
            if str(username).lower() in line.lower():
                user_found = True
                userdata_str = line
                while True:
                    line = userdata_file_reader.readline()
                    userdata_str += line
                    if '}' in line:
                        break
                break
            line = userdata_file_reader.readline()

        userdata_file_reader.close()

        if user_found == False:
            # User not found in file so initialising to dictionary with error
            self.userdata = {'ERROR' : 'USER NOT FOUND'}
        else:
            userdata_str = userdata_str.split('{')[1].split('}')[0]
            userdata_arr = userdata_str.split(';')

            for data in userdata_arr:
                if '=' in data:
                    data = data.lstrip().rstrip()
                    key = data.split('=')[0]
                    key = key.lstrip().rstrip()
                    if '\n' in key:
                        key = key.replace('\n','')
                    if '\t' in key:
                        key = key.replace('\t','')
                    if ' ' in key:
                        key = key.replace(' ','')
                    val = data.split('=')[1].rstrip()
                    if '"' in val:
                        val = data.split('"',1)[1].split('"')[0]
                    self.userdata[key] = val

        available_userdata_keys = []
        for key in self.userdata:
            available_userdata_keys.append(key)

        required_userdata_keys = find_userdata_vars_required_in_lib()

        for key in required_userdata_keys:
            if key == 'phonenumber':
               try:
                   self.userdata['phonenumber'] = self.userdata['extension']
               except:
                   self.userdata[key] = "<VALUE MISSING IN USERDATA>"
            elif key not in available_userdata_keys:
                try:
                    value = getattr(Data, key)
                    self.userdata[key] = value
                except:
                    self.userdata[key] = "<VALUE MISSING IN USERDATA>"

        #print(str(self.userdata))


class Host:
    def __init__(self,ip, port, playID, recordID,speechVerification,mobileSpeechVerification):
        self.ip = ip
        self.port = port
        self.playID = playID
        self.recordID = recordID
        self.speechVerification = speechVerification
        self.mobileSpeechVerification = mobileSpeechVerification
