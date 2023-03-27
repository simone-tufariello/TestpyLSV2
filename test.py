#!/bin/python3
from NC import NC
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ip = "192.168.1.40"
tnc = NC(ip)
tnc.Connect()

print(bcolors.BOLD +"\nCNC information: " + bcolors.ENDC)
print("[*] " + bcolors.OKGREEN +"Machine Model: " + bcolors.ENDC  + tnc.con.versions.control)
print("[*] " + bcolors.OKGREEN +"Machine Software Version: " + bcolors.ENDC + tnc.con.versions.nc_sw)
print("[*] " + bcolors.OKGREEN +"Machine LSV2 Version: " + bcolors.ENDC + str(tnc.con.parameters.lsv2_version))

print(bcolors.BOLD + "\nProgram information: " + bcolors.ENDC + bcolors.ENDC)
print("[*] " + bcolors.OKGREEN +"Axes Position: " + bcolors.ENDC + str(tnc.con.axes_location()))
print("[*] " + bcolors.OKGREEN +"Current NC Program: " + bcolors.ENDC + str(tnc.con.program_stack()))
t_info = tnc.con.spindle_tool_status()
print("[*] " + bcolors.OKGREEN +"Current Tool in spindle: " + bcolors.ENDC + "{:d}.{:d} '{:s}'".format(
        t_info.number, t_info.index, t_info.name))

if tnc.con.versions.is_itnc():
    e_m = tnc.con.get_error_messages()
    print("[*] " + bcolors.OKGREEN +"Number of active Error Messages: " + bcolors.ENDC +"{:d}".format(len(e_m)))
    for i, msg in enumerate(e_m):
        print("\t- Error {:d} : {:s}".format(i, str(msg)))
else:
    print("[!] Number of active Error Messages: \n    Function 'get_error_messages()' not suportet for this control")


dir_content = tnc.con.directory_content()
only_files = filter(
    lambda f_e: f_e.is_directory is False and f_e.is_drive is False,
    dir_content,
)

print("\n[*] " + bcolors.OKGREEN +"List files in: /TNC/nc_prog/" + bcolors.ENDC)
for file_entry in only_files:
    print(
        "\t- file name: {:s},  \tdate {:}, \tsize {:d} bytes".format(
            file_entry.name, file_entry.timestamp, file_entry.size
        )
    )
only_dir = filter(
    lambda f_e: f_e.is_directory is True and f_e.is_drive is False, dir_content
)
print("\n")
for file_entry in only_dir:
    print(
        "\t- directory name: {:s}, \tdate {:}".format(
            file_entry.name, file_entry.timestamp
        )
    )
print("\n\n")




        
            
    