import os
import datetime
from pathlib import Path
import pygetwindow as gw
import pyperclip

def save_urls():
    #Activate the Firefox window
    firefox_windows = gw.getWindowsWithTitle('')
    for win in firefox_windows:
        if "Mozilla Firefox" in win.title:
            win.activate()
            break

    #Assuming you've set Ctrl+Shift+U as the shortcut to copy all the URLs
    os.system("keybd_event 0x11 0 0 0") # Ctrl
    os.system("keybd_event 0x10 0 0 0") # Shift
    os.system("keybd_event 0x55 0 0 0") # U
    os.system("keybd_event 0x55 0 0 0") # -U
    os.system("keybd_event 0x10 0 0 0") # -Shift
    os.system("keybd_event 0x11 0 0 0") # -Ctrl

    #Get the copied URLs
    urls = pyperclip.paste()

    #Create an 'output' folder if the doesn't exist
    Path("output").mkdir(parents=True, exist_ok=True)

    #Save the URLs in a dated .txt file in 'output' folder
    with open(f"outptu/{datetime.date.today()}.txt", "w") as file:
        file.write(urls)

if __name__ == "__main__":
    save_urls()