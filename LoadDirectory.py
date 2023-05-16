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
os.system("mkdir "+OutFolder)
time.sleep(2)
i=1
for file in directories:
    if(file.endswith(".mp4")):
        InVideoFile = os.path.join(InFolder,file).replace("/","\\")
        OutVideoFile = os.path.join(OutFolder,file).replace("/","\\")
        print("Staring Process ",str(i),"->",InVideoFile,"->",OutVideoFile)
        
        os.system("VideoConverter.exe -i "+ InVideoFile +" -metadata FRAMERATE=25/1 -metadata RESOLUTION=1920x1080 -metadata title=\"traffic\" -metadata artist=\"kad\" -metadata year=\"2023\" -c:v copy -c:a copy " + OutVideoFile)
        i=i+1

exit()
