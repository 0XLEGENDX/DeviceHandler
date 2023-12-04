import subprocess
import time

#This deviceController uses adb for shell commands, if you don't have it then install it.

def powerButton():
    
    subprocess.Popen('adb shell input keyevent 26',shell=True)


#This openMenu is only for swipeUp Devices
def openMenu():
    
    
    subprocess.Popen("adb shell input tap 344 966",shell=True)
    

# powerButton()
# time.sleep(5)
openMenu()



