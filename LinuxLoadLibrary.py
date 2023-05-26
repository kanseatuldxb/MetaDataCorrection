import os #<-- this Process all Folder's MP4 Structure in Other Destination. 
import time


def OperationsProcess(InFolder):
    directories = os.listdir( InFolder )
    print(directories)
    time.sleep(2)
    i=1
    for file in directories:
        if(file.endswith(".mp4")):
            InVideoFile = os.path.join(InFolder,file)
            OutVideoFile = os.path.join(InFolder,file).replace("/media/tektronix/Extreme Pro/DXB2040","/media/tektronix/Extreme Pro1/DXB2040")
            print("Staring Process ",str(i),"->",InVideoFile,"->",OutVideoFile)
            os.system("ffmpeg -i \""+ InVideoFile +"\" -metadata FRAMERATE=25/1 -metadata RESOLUTION=1920x1080 -metadata title=\"traffic\" -metadata artist=\"kad\" -metadata year=\"2023\" -c:v copy -c:a copy \"" + OutVideoFile+"\"")
            i=i+1

drive_path = "/media/tektronix/Extreme Pro"  # Replace "C:" with the desired drive path
dest_drive_path = "/media/tektronix/Extreme Pro1"

for root, dirs, files in os.walk(drive_path):
    print(root,root.startswith("/media/tektronix/Extreme Pro/DXB2040"))
    if root.startswith("/media/tektronix/Extreme Pro/DXB2040"):
        folder_path = root
        file_count = len(files)
        print(f"Folder: {folder_path}")
        OperationsProcess(folder_path)



exit()




import os #<-- this Copies all Folder Structure in Other Destination. 

drive_path = "/media/tektronix/Extreme Pro"  # Replace "C:" with the desired drive path
dest_drive_path = "/media/tektronix/Extreme Pro1"

for root, dirs, files in os.walk(drive_path):
    print(root,root.startswith("/media/tektronix/Extreme Pro/DXB2040"))
    if root.startswith("/media/tektronix/Extreme Pro/DXB2040"):
        folder_path = root
        file_count = len(files)
        print(f"Folder: {folder_path}")
        if not os.path.exists(root.replace(drive_path,dest_drive_path)):
            os.system("mkdir \""+root.replace(drive_path,dest_drive_path)+"\"")


exit()


import os #<-- this check all the source files generated or not
import time


def OperationsProcess(InFolder):
    directories = os.listdir( InFolder )
    #print(directories)
    #time.sleep(2)
    i=1
    for file in directories:
        if(file.endswith(".mp4")):
            InVideoFile = os.path.join(InFolder,file)
            OutVideoFile = os.path.join(InFolder,file).replace("/media/tektronix/My Passport/DXB2024","/media/tektronix/My Passport1/DXB2024")
            if not os.path.isfile(OutVideoFile):
                print("Staring Process ",str(i),"->",InVideoFile,"->",OutVideoFile)
           
            #os.system("VideoConverter.exe -i \""+ InVideoFile +"\" -metadata FRAMERATE=25/1 -metadata RESOLUTION=1920x1080 -metadata title=\"traffic\" -metadata artist=\"kad\" -metadata year=\"2023\" -c:v copy -c:a copy \"" + OutVideoFile+"\"")
            i=i+1

drive_path = "/media/tektronix/My Passport/DXB2024"  # Replace "C:" with the desired drive path
dest_drive_path = "/media/tektronix/My Passport1/DXB2024"

for root, dirs, files in os.walk(drive_path):
    if root.startswith("/media/tektronix/My Passport/DXB2024"):
        folder_path = root
        file_count = len(files)
        #print(f"Folder: {folder_path}")
        OperationsProcess(folder_path)



exit()






import os #<-- this Process all Folder's MP4 Structure in Other Destination. 
import time


def OperationsProcess(InFolder):
    directories = os.listdir( InFolder )
    print(directories)
    time.sleep(2)
    i=1
    for file in directories:
        if(file.endswith(".mp4")):
            InVideoFile = os.path.join(InFolder,file)
            OutVideoFile = os.path.join(InFolder,file).replace("/media/tektronix/My Passport/DXB2024","/media/tektronix/My Passport1/DXB2024")
            print("Staring Process ",str(i),"->",InVideoFile,"->",OutVideoFile)
            os.system("ffmpeg -i \""+ InVideoFile +"\" -metadata FRAMERATE=25/1 -metadata RESOLUTION=1920x1080 -metadata title=\"traffic\" -metadata artist=\"kad\" -metadata year=\"2023\" -c:v copy -c:a copy \"" + OutVideoFile+"\"")
            i=i+1

drive_path = "/media/tektronix/My Passport"  # Replace "C:" with the desired drive path
dest_drive_path = "/media/tektronix/My Passport1"

for root, dirs, files in os.walk(drive_path):
    print(root,root.startswith("/media/tektronix/My Passport/DXB2024"))
    if root.startswith("/media/tektronix/My Passport/DXB2024"):
        folder_path = root
        file_count = len(files)
        print(f"Folder: {folder_path}")
        OperationsProcess(folder_path)



exit()


import os #<-- this Copies all Folder Structure in Other Destination. 

drive_path = "/media/tektronix/My Passport"  # Replace "C:" with the desired drive path
dest_drive_path = "/media/tektronix/My Passport1"

for root, dirs, files in os.walk(drive_path):
    print(root)
    if root.startswith("/media/tektronix/My Passport/DXB2024"):
        folder_path = root
        file_count = len(files)
        print(f"Folder: {folder_path}")
        if not os.path.exists(root.replace(drive_path,dest_drive_path)):
            os.system("mkdir \""+root.replace(drive_path,dest_drive_path)+"\"")


exit()




import os #<-- this check all the source files generated or not
import time


def OperationsProcess(InFolder):
    directories = os.listdir( InFolder )
    #print(directories)
    #time.sleep(2)
    i=1
    for file in directories:
        if(file.endswith(".mp4")):
            InVideoFile = os.path.join(InFolder,file).replace("/","\\")
            OutVideoFile = os.path.join(InFolder,file).replace("/","\\").replace("E:DXB2024","F:DXB2024")
            if not os.path.isfile(OutVideoFile):
                print("Staring Process ",str(i),"->",InVideoFile,"->",OutVideoFile)
           
            #os.system("VideoConverter.exe -i \""+ InVideoFile +"\" -metadata FRAMERATE=25/1 -metadata RESOLUTION=1920x1080 -metadata title=\"traffic\" -metadata artist=\"kad\" -metadata year=\"2023\" -c:v copy -c:a copy \"" + OutVideoFile+"\"")
            i=i+1

drive_path = "E:"  # Replace "C:" with the desired drive path
dest_drive_path = "F:"

for root, dirs, files in os.walk(drive_path):
    if root.startswith("E:DXB2024"):
        folder_path = root
        file_count = len(files)
        #print(f"Folder: {folder_path}")
        OperationsProcess(folder_path)



exit()

import os
import numpy as np
import time
import tkinter as tk
from tkinter import filedialog

print('''
made by 
 _                              _         _     _      _     
| | ____ _ _ __  ___  ___  __ _| |_ _   _| | __| |_  _| |__  
| |/ / _` | '_ \/ __|/ _ \/ _` | __| | | | |/ _` \ \/ / '_ \ 
|   < (_| | | | \__ \  __/ (_| | |_| |_| | | (_| |>  <| |_) |
|_|\_\__,_|_| |_|___/\___|\__,_|\__|\__,_|_|\__,_/_/\_\_.__/ 
''')

root = tk.Tk()
root.withdraw()

InFolder = filedialog.askdirectory()
print(InFolder)

directories = os.listdir( InFolder )


OutFolder = os.path.join(InFolder,"Output").replace("/","\\")
os.system("mkdir \""+OutFolder+"\"")
time.sleep(2)
i=1
for file in directories:
    if(file.endswith(".mp4")):
        InVideoFile = os.path.join(InFolder,file).replace("/","\\")
        OutVideoFile = os.path.join(OutFolder,file).replace("/","\\")
        print("Staring Process ",str(i),"->",InVideoFile,"->",OutVideoFile)
        
        os.system("VideoConverter.exe -i \""+ InVideoFile +"\" -metadata FRAMERATE=25/1 -metadata RESOLUTION=1920x1080 -metadata title=\"traffic\" -metadata artist=\"kad\" -metadata year=\"2023\" -c:v copy -c:a copy \"" + OutVideoFile+"\"")
        i=i+1




import os #<-- this Copies all Folder Structure in Other Destination. 

drive_path = "E:"  # Replace "C:" with the desired drive path
dest_drive_path = "F:"

for root, dirs, files in os.walk(drive_path):
    if root.startswith("E:DXB2024"):
        folder_path = root
        file_count = len(files)
        print(f"Folder: {folder_path}")
        if not os.path.exists(root.replace(drive_path,dest_drive_path)):
            os.system("mkdir \""+root.replace(drive_path,dest_drive_path)+"\"")


exit()



