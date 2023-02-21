import pyLSV2

class NC:
    def __init__(self, host):
        self.host = host
        self.con = pyLSV2.LSV2(host, port=19000, safe_mode=False)

    def Connect(self):
        self.con.connect()

    def Disconnect(self):
        self.con.disconnect()

    def Layout(self, title):
        self.title = title
        print("-"*50, f"\n{title}:")

    def NCSoftwareVersion(self):   
        self.Layout("NC and Software Version")
        print(
            "[*] Connected to a '{:s}' running software version '{:s}'".format(
                self.con.versions.control, self.con.versions.nc_sw
            )
        )
        print("-"*50,"\n")
        

    def LSV2Version(self):
        self.Layout("LSV2 Version")
        print(
            "[*] Using LSV2 version '{:d}' with version flags '0x{:02x}' and '0x{:02x}'".format(
                self.con.parameters.lsv2_version,
                self.con.parameters.lsv2_version_flags,
                self.con.parameters.lsv2_version_flags_ex,
            )
        )
        print("-"*50,"\n")

    def GetAxesPosition(self):
        self.Layout("AXES Positions")
        print("[*] Axes positions: {}".format(self.con.axes_location()))
        print("-"*50,"\n")
    
    def getActiveNCProgram(self):
        self.Layout("Current Active NC Program")
        NCProg = self.con.program_stack()
        if NCProg == False:
            print("Error in reading current active NC program")
        else:
            print(NCProg)
        print("-"*50,"\n")

    def CurrentDirectory(self):
        self.Layout("Current Directory")
        drv_info = self.con.drive_info()
        print(
            "[*] Names of disk drives: {:s}".format(
                ", ".join([drv.name for drv in drv_info])
            )
        )
        dir_info = self.con.directory_info()
        print(
            "[*] Current directory is '{:s}' with {:d} bytes of free drive space".format(
                dir_info.path, dir_info.free_size
            )
        )
        print("-"*50,"\n")

    def ChangeDirectory(self):
        self.Layout("Change Current Directory")
        login = self.con.login("FILE")
        directory = r"../"
        dir = self.con.change_directory(directory)
        if dir:
            print("OK")
        else:
            print("KO")
        print("-"*50,"\n")

    def DonwloadFile(self):
        self.Layout("Download file from Simulator")
        login = self.con.login("FILE")
        remotePathFile = r"TOOL.H"
        localPathSave = r"D:/Università/Tirocinio/Heidenhain/Codice/VSCode/LSV2py/TestTransfer/TOOL.H"
        transfer = self.con.recive_file(remotePathFile, localPathSave, override_file=False, binary_mode=False)
        if transfer:
            print("Transfer completed successfully")
        else:
            print("Error in copying file")
        print("-"*50,"\n")

    def UploadFile(self):
        self.Layout("Upload file to Simulator")
        localPath = r"D:\Università\Tirocinio\Heidenhain\Codice\VSCode\LSV2py\TestTransfer\Ciao.txt"
        remotePathFile = r"Ciao.txt"
        login = self.con.login("FILE")
        send = self.con.send_file(localPath, remotePathFile, override_file=True, binary_mode=False)
        if send:
            print("Upload completed successfully in TNC:/nc_prog")
        print("-"*50,"\n")

    def ExecuteCommand(self):
        self.Layout("Execute Command")
        self.con.set_keyboard_access(False)
        comando = self.con.send_key_code(pyLSV2.KeyCode.BOTTOM_SK3)
        self.con.set_keyboard_access(True)
        if comando:
            print("Command successfully executed")
        else:
            print("Command NOT properly executed")
        print("-"*50,"\n")

    def SwitchSafeMode(self):
        self.Layout("Switch OFF Safe Mode")
        print(self.con.switch_safe_mode(enable_safe_mode=False))
        print("-"*50,"\n")

    def Login(self):
        login = self.con.login("FILE", "testheide")
        if login:
            print("OK")
        else:
            print("KO")
       
