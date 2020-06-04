import os

def get_file_reader_for_msm(client_name):
    cwd = os.getcwd()
    files_dir_path = cwd.split('\svauto')[0] + "\svauto\SoftClients\SoftClients_MSMPlugin\SoftClient_MSM\customer"
    file_reader = open(files_dir_path + "\\" + client_name + "_MSM.java", "r")
    return file_reader

def get_file_reader_for_client_python_lib(client_name):
    cwd = os.getcwd()
    files_dir_path = cwd.split('\SOCKETBOT')[0] + "\SOCKETBOT\CLIENTS\SOCKET_IMPLEMENTED"
    file_reader = open(files_dir_path + "\\" + client_name + ".py", "r")
    return file_reader

def write_to_map_file(client_name,line):
    files_dir_path = os.getcwd() + "\CONVERTER_MAP_FILES"
    file_writer = open(files_dir_path + "\\" + client_name + "_function_map.txt", "a")
    file_writer.write(str(line) + '\n')

def get_msm_function_name(input):
    func_name = str(input).split("(")[0]
    func_name = func_name.split(" ")[3]
    return func_name

def get_python_def_name(input):
    func_name = str(input).split("(")[0]
    func_name = func_name.split("def ")[1]
    func_name = func_name.replace("_",'')
    if "acw" in func_name:
        func_name = func_name.replace("acw",'')
    if "acm" in func_name:
        func_name = func_name.replace("acm",'')
    if "aca" in func_name:
        func_name = func_name.replace("aca",'')
    if "aci" in func_name:
        func_name = func_name.replace("aci",'')
    return func_name.lower()


def get_python_def_from_file(client,function):
    python_file_reader = get_file_reader_for_client_python_lib(client)
    i = 0
    line = python_file_reader.readline()
    py_def_found = False
    py_def_name = ''
    param_list = []
    while line:
        function_name = ''
        line = python_file_reader.readline()
        try:
            if "def" in line:
                if str(function).split("_")[1].lower() in str(get_python_def_name(line)):
                    func_line = line.split(")")[0]
                    param_list = func_line.split("(")[1].split(",")
                    if len(param_list) < 2:
                        param_list = []
                    else:
                        param_list = param_list[1:(len(param_list) - 1)]
                    py_def_name = line.split("(")[0]
                    py_def_name = py_def_name.split("def ")[1]
                    print("$$$$$$"+"PYTHON_DEF_FOUND;" + str(function) + ';' + py_def_name + ';' + str(param_list) + ';'+"$$$$$$")
                    py_def_found = True
                    break
                else:
                    line = python_file_reader.readline()
                    continue
        except:
            print("*********"+"PYTHON_DEF_NOT_FOUND;" + function+"*********")
            return "PYTHON_DEF_NOT_FOUND;" + function

    if py_def_found:
        return "<FUNCTION_FOUND>        PYTHON_DEF_FOUND;" + str(function) + ';' + py_def_name + ';' + str(param_list) + ';'
    else:
        return "<FUNCTION_NOT_IN_PY_FILE>       PYTHON_DEF_NOT_FOUND;" + str(function)


def create_function_map_file(msm_name,py_lib_name):
    msm_file_reader = get_file_reader_for_msm(msm_name)

    # Create funcion map file before every run.
    files_dir_path = os.getcwd() + "\CONVERTER_MAP_FILES"
    open(files_dir_path + "\\" + msm_name + "_function_map.txt", "w").close()

    i = 0
    line = msm_file_reader.readline()

    while line:
        function_name = ''
        try:
            is_irregular = False
            if "public synchronized void" in line:
                function = line
                while('}' not in line):
                    # skipping commented out lines
                    line = msm_file_reader.readline()
                    if '/' in line:
                        continue
                    # this will skip block comments
                    elif '/*' in line:
                        while '*/' not in line:
                            line = msm_file_reader.readline()
                            continue
                    elif '{' in line:
                        while('}' not in line):
                            is_irregular = True
                            function = function + line
                            line = msm_file_reader.readline()
                    else:
                        i = i + 1
                        function = function + line
                function_name = get_msm_function_name(function)
                if is_irregular:
                    write_to_map_file(msm_name,"<IRREGULAR>        PYTHON_DEF_NOT_AVAILABLE;" + function_name)
                    line = msm_file_reader.readline()
                    is_irregular = False
                    continue
                out = get_python_def_from_file(py_lib_name, function_name)
                write_to_map_file(msm_name, out)
        except:
            write_to_map_file(msm_name, "<EXCEPTION>        PYTHON_DEF_NOT_AVAILABLE;" + function_name)
        line = msm_file_reader.readline()


#create_function_map_file("ACW","WINDOWS")
#create_function_map_file("ACM","MAC")
#create_function_map_file("ACA","ANDROID")
#create_function_map_file("ACI","IOS")

def validate_maps():
    aca_file_reader = open("C:/SVAUTO/svauto/SOCKETBOT/UTILITY/CONVERTER_MAP_FILES/ACA_Function_map_Manually_Corrected.txt",'r')
    line = aca_file_reader.readline()
    while line:
        if '\n' in line:
            line = line.split('\n')[0]
        line = line.replace(' ','')
        arr = line.split(';')
        if len(arr) > 5 and "FUNCTION_FOUND" in line:
            print(str(arr))
            print("Wrong line :- " + line)
        line = aca_file_reader.readline()
    aca_file_reader.close()

    acw_file_reader = open(
        "C:/SVAUTO/svauto/SOCKETBOT/UTILITY/CONVERTER_MAP_FILES/ACW_Function_map_Manually_Corrected.txt", 'r')
    line = acw_file_reader.readline()
    while line:
        if '\n' in line:
            line = line.split('\n')[0]
        arr = line.split(';')
        if len(arr) > 5 and "FUNCTION_FOUND" in line:
            print(str(arr))
            print("Wrong line :- " + line)
        line = acw_file_reader.readline()
    acw_file_reader.close()

    acm_file_reader = open(
        "C:/SVAUTO/svauto/SOCKETBOT/UTILITY/CONVERTER_MAP_FILES/ACM_Function_map_Manually_Corrected.txt", 'r')
    line = acm_file_reader.readline()
    while line:
        if '\n' in line:
            line = line.split('\n')[0]
        arr = line.split(';')
        if len(arr) > 5 and "FUNCTION_FOUND" in line:
            print(str(arr))
            print("Wrong line :- " + line)
        line = acm_file_reader.readline()
    acm_file_reader.close()

    aci_file_reader = open(
        "C:/SVAUTO/svauto/SOCKETBOT/UTILITY/CONVERTER_MAP_FILES/ACI_Function_map_Manually_Corrected.txt", 'r')
    line = aci_file_reader.readline()
    while line:
        if '\n' in line:
            line = line.split('\n')[0]
        arr = line.split(';')
        if len(arr) > 5 and "FUNCTION_FOUND" in line:
            print(str(arr))
            print("Wrong line :- " + line)
        line = aci_file_reader.readline()
    aci_file_reader.close()


def find_userdata_vars_required_in_lib():
    cwd = os.getcwd()
    path = str(cwd).split('SOCKETBOT')
    file_reader = open(path[0] + 'SOCKETBOT\CLIENTS\SOCKET_IMPLEMENTED\ANDROID.py', 'r')
    line = file_reader.readline()
    aca_userdata_fields = []
    while line:
        if 'self.userdata[' in line:
            arrs = line.split('self.userdata')
            for arr in arrs:
                if "['" in arr and "']" in arr:
                    arr = arr.split("['")[1].split("']")[0]
                    if arr not in aca_userdata_fields:
                        aca_userdata_fields.append(arr)
        line = file_reader.readline()
    file_reader.close()
    # print("ACA_USERDATA_NEEDED:-" + str(aca_userdata_fields) + '\n\n')

    file_reader = open(path[0] + 'SOCKETBOT\CLIENTS\SOCKET_IMPLEMENTED\MAC.py', 'r')
    line = file_reader.readline()
    acm_userdata_fields = []
    while line:
        if 'self.userdata[' in line:
            arrs = line.split('self.userdata')
            for arr in arrs:
                if "['" in arr and "']" in arr:
                    arr = arr.split("['")[1].split("']")[0]
                    if arr not in acm_userdata_fields:
                        acm_userdata_fields.append(arr)
        line = file_reader.readline()

    # print("ACM USERDATA NEEDED :- " + str(acm_userdata_fields) + '\n\n')
    file_reader.close()

    file_reader = open(path[0] + 'SOCKETBOT\CLIENTS\SOCKET_IMPLEMENTED\WINDOWS.py', 'r')
    line = file_reader.readline()
    acw_userdata_fields = []
    while line:
        if 'self.userdata[' in line:
            arrs = line.split('self.userdata')
            for arr in arrs:
                if "['" in arr and "']" in arr:
                    arr = arr.split("['")[1].split("']")[0]
                    if arr not in acw_userdata_fields:
                        acw_userdata_fields.append(arr)
        line = file_reader.readline()
    file_reader.close()

    # print("ACW_USERDATA_NEEDED:-" + str(acw_userdata_fields) + '\n\n')

    file_reader = open(path[0] + 'SOCKETBOT\CLIENTS\SOCKET_IMPLEMENTED\IOS.py', 'r')
    line = file_reader.readline()
    aci_userdata_fields = []
    while line:
        if 'self.userdata[' in line:
            arrs = line.split('self.userdata')
            for arr in arrs:
                if "['" in arr and "']" in arr:
                    arr = arr.split("['")[1].split("']")[0]
                    if arr not in aci_userdata_fields:
                        aci_userdata_fields.append(arr)
        line = file_reader.readline()
    file_reader.close()

    # print("ACI_USERDATA_NEEDED:-" + str(aci_userdata_fields) + '\n\n')

    total_userdara_fields = []
    for data in acw_userdata_fields:
        if data not in total_userdara_fields:
            total_userdara_fields.append(data)

    for data in acm_userdata_fields:
        if data not in total_userdara_fields:
            total_userdara_fields.append(data)

    for data in aca_userdata_fields:
        if data not in total_userdara_fields:
            total_userdara_fields.append(data)

    for data in aci_userdata_fields:
        if data not in total_userdara_fields:
            total_userdara_fields.append(data)

    # print("TOTAL_USERDATA_NEEDED:-" + str(total_userdara_fields) + '\n\n')
    return total_userdara_fields

#validate_maps()
#find_userdata_vars_required_in_lib()