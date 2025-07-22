import subprocess as sp
import webbrowser as Linkexecuter
import pyfirmata2 as pyf
# from threading import Timer
import time as t
from PIL import ImageGrab
   
class ProtocolExecuteLink:
    def __init__(self, link):
        self.link = link

    def loadLink(self):
        Linkexecuter.open(self.link)

class ProtocolExecuteFile:
    def __init__(self, FilePath):
        self.FilePath = FilePath
    
    def ExecuteFileC(self, exeFilePath):
        sp.call(["gcc", self.FilePath, "-o", exeFilePath])
        sp.call([exeFilePath])

    def ExecuteFilepy(self):
        sp.call(["python", self.FilePath])

    def WriteFile(self, content):
        file = open(self.FilePath, "w")
        file.write(content)
        file.close()
    
    def Removelines(self):
        with open(self.FilePath, 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:-1])
    
    def Screenshot(self,n):
        img = ImageGrab.grab()
        img.save(f"screenshot{n}.png")
        n += 1

            

class ProtocolHardwareAccess:
    def __init__(self):
        self.PORT =  pyf.Arduino.AUTODETECT
        self.board = pyf.Arduino(self.PORT)
    
    def selectPin(self, pin, mode):
        portSet = self.board.get_pin(f'd:{pin}:{mode}')
        return portSet

    def SetPowerPin(self, pow, pin, mode):
        ps = self.selectPin(pin, mode)
        ps.write(pow)
    
    def SetPowerToggle(self, n, time , pin, mode):
        ps = self.selectPin(pin, mode)
        for write in range(n):
            ps.write(pow)
            t.sleep(time)






