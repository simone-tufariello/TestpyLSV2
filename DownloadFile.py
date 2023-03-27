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

tnc.Screenshot()

#print(bcolors.BOLD +"\nDonwload Program from CNC: " + bcolors.ENDC)
#tnc.DownloadProgram()

# /mnt/tnc/nc_prog/SAFE.H
# D:/Università/Tirocinio/Heidenhain/Codice/VSCode/LSV2py/TestTransfer/SAFE.H