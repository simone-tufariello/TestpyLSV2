import pyLSV2

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

class NC:
    def __init__(self, host):
        self.host = host
        self.con = pyLSV2.LSV2(host, port=19000, safe_mode=False)

    def Connect(self):
        print(f"\nConnecting to ip {self.host}...")
        conn = self.con.connect()
        # print("-"*50,"\n")

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
        comando = self.con.send_key_code(pyLSV2.KeyCode.MODE_SINGLE_STEP)
        self.con.set_keyboard_access(True)
        if comando:
            print("Command successfully executed")
        else:
            print("Command NOT properly executed")
        print("-"*50,"\n")

    def SwitchSafeMode(self):
        self.Layout("Switch OFF ON* Safe Mode")
        print(self.con.switch_safe_mode(enable_safe_mode=False))
        print("-"*50,"\n")

    def ReadErrMex(self):
        self.Layout("Read Error Messages")
        if self.con.versions.is_itnc():
            e_m = self.con.get_error_messages()
            print("[*] Number of currently active error messages: {:d}".format(len(e_m)))
            for i, msg in enumerate(e_m):
                print("[*] Error {:d} : {:s}".format(i, str(msg)))
        else:
            print("[!!] function 'get_error_messages()' not suportet for this control \n     Only available on iTNC530")

        print("-"*50,"\n")

    def ReadToolSpindle(self):
        self.Layout("Read Spindle Tool Information")
        t_info = self.con.spindle_tool_status()
        if t_info is not None:
            print("[*] Direct reading of current tool successful")
            print(
                "[*] current tool in spindle: {:d}.{:d} '{:s}'".format(
                    t_info.number, t_info.index, t_info.name
                )
            )
        else:
            print("[!!] Direct reading of current tool not supported for this control")

        print("-"*50,"\n")

    def ListFile(self):
        self.Layout("List files in: /TNC/nc_prog/")
        dir_content = self.con.directory_content()
        only_files = filter(
            lambda f_e: f_e.is_directory is False and f_e.is_drive is False,
            dir_content,
        )

        for file_entry in only_files:
            print(
                "\t- file name: {:s}, \t date {:}, \t size {:d} \t bytes".format(
                    file_entry.name, file_entry.timestamp, file_entry.size
                )
            )
        only_dir = filter(
            lambda f_e: f_e.is_directory is True and f_e.is_drive is False, dir_content
        )
        print("\n")
        for file_entry in only_dir:
            print(
                "\t- \t directory name: {:s}, \t date {:}".format(
                    file_entry.name, file_entry.timestamp
                )
            )
        print("-"*50,"\n")

    def GetExecMode(self):
        self.Layout("Get Execution Mode and Program Runnig")
        exec_stat = self.con.execution_state()
        exec_stat_text = pyLSV2.get_execution_status_text(exec_stat)
        print("[*] execution: {:d} - '{:s}'".format(exec_stat, exec_stat_text))
        pgm_stat = self.con.program_status()
        if pgm_stat is not None:
            pgm_stat_text = pyLSV2.get_program_status_text(pgm_stat)
            print("[*] program: {:d} - '{:s}'".format(pgm_stat, pgm_stat_text))
        print("-"*50,"\n")

    def test(self):
        self.Layout("Test:")
        pathFile = r"TOOL.H"
        print(self.con.file_info(pathFile))
        print("-"*50,"\n")

    def MakeDirectory(self):
        self.Layout("Create a directory")
        pathDir = r"PROVA"
        makeDir = self.con.make_directory(pathDir)
        if(makeDir):
            print("Folder created correctly")
        else:
            print("Error in folder creation")        
        
        print("-"*50,"\n")

    def DeleteFile(self):
        self.Layout("Delete file")
        delFile = r"Ciao.txt"
        deliteFile = self.con.delete_file(delFile)
        if(deliteFile):
            print("File deleted successfully")
        else:
            print("Error in deleting the file")        
        
        print("-"*50,"\n")
        
    def ReadMachineParam(self):
        self.Layout("Read Machine Parameter")
        nameParam = "100"
        delFile = self.con.get_machine_parameter(nameParam)
        print(delFile)     
        
        print("-"*50,"\n")    

    def ScreenShot(self):
        self.Layout("Take a ScreenShot")
        pathToSave = r"nc_prog"
        screen = self.con.grab_screen_dump(pathToSave)
        print(screen)
        if(screen):
            print("Screenshot successfully executed")
        else:
            print("Error in making screenshot")   
        
        print("-"*50,"\n")    


    def Login(self):
        login = self.con.login("FILE", "testheide")
        if login:
            print("OK")
        else:
            print("KO")
    





    def DownloadProgram(self):
        login = self.con.login("FILE")
        remotePathFile = input(bcolors.OKGREEN + "Enter path to remote file: " + bcolors.ENDC)
        
        localPathSave = input(bcolors.OKGREEN + "Enter save path: "  + bcolors.ENDC)
        transfer = self.con.recive_file(remotePathFile, localPathSave, override_file=True, binary_mode=False)
        if transfer:
            print("\n[*] Transfer completed successfully")
        else:
            print("\t[!] Error in downloading file")
        print("-"*50,"\n")


    def Screenshot(self):
        localPathSave = input(bcolors.OKGREEN + "Enter save path: "  + bcolors.ENDC)
        localPathSave = r"temp"
        screen = self.con.grab_screen_dump(localPathSave)
        