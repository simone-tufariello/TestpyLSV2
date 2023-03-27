#!/bin/python3
from NC import NC

ip = input("Enter IP NC: ")
ip = "192.168.1.40"
tnc = NC(ip)
tnc.Connect()

while(True):
    print("""[1] NC and Software version
[2] LSV2 version
[3] Get Axes Positions
[4] Get Active NC Program
[5] Get Current Directory
[6] Change Directory
[7] Make Directory
[8] Download File
[9] Upload File
[10] Delete File
[11] List Files
[12] Read Error Messages
[13] Get Execution Mode and Program Runnig
[14] Execute Command
[15] Read Machine Parameter
[16] Get Current Tool in spindle
[17] Take Screendshot
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
            tnc.MakeDirectory()
        case "8":
            tnc.DonwloadFile()
        case "9":
            tnc.UploadFile()
        case "10":
            tnc.DeleteFile()
        case "11":
            tnc.ListFile()
        case "12":
            tnc.ReadErrMex()
        case "13":
            tnc.GetExecMode()
        case "14":
            tnc.ExecuteCommand()
        case "15":
            tnc.ReadMachineParam()
        case "16":
            tnc.ReadToolSpindle()
        case "17":
            tnc.ScreenShot()
        case "18":
            tnc.test()
        case "99":
            break
        case _:
            print("Err")

tnc.Disconnect()


