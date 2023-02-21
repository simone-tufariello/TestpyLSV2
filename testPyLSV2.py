#!/bin/python3
from NC import NC

# ip = input("Enter IP NC: ")
ip = "192.168.1.30"
tnc = NC(ip)
tnc.Connect()

while(True):
    print("""[1] NC and Software version
[2] LSV2 version
[3] Get Axes Positions
[4] Get Active NC Program
[5] Get Current Directory
[6] Change Directory
[7] Download File
[8] Upload File
[9] Execute Command
[10] Switch Safe Mode
[99] Exit
""")
    try:
        action = input("Enter number: ")
    except KeyboardInterrupt:
        break

    match action:
        case "1":
            tnc.NCSoftwareVersion()
        case "2":
            tnc.LSV2Version()
        case "3":
            tnc.GetAxesPosition()
        case "4":
            tnc.getActiveNCProgram()
        case "5":
            tnc.CurrentDirectory()
        case "6":
            tnc.ChangeDirectory()
        case "7":
            tnc.DonwloadFile()
        case "8":
            tnc.UploadFile()
        case "9":
            tnc.ExecuteCommand()
        case "10":
            tnc.SwitchSafeMode()
        case "99":
            break
        case _:
            print("Err")

tnc.Disconnect()