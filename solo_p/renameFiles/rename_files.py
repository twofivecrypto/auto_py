#! Python 3.11
# We are going to walk through a folder directory and rename the png files 
# in the folder in order to rename them as 'astora_brand_identity.xxx' where 'x' represents
# the png order.

import os, shutil

folder_path = r"C:\Users\94M0\Downloads\astorabrandidentity\astora_brand"
new_template = "astora_brand_identity.{}.png"

#Get a list of all the files in the folder
file_list = os.listdir(folder_path)

#Filter PNG files from the list
png_files = [file for file in file_list if file.lower().endswith(".png")]

#Sort the list of PNG files
png_files.sort()

#Rename and move the files
for index, old_name in enumerate(png_files, start=1):
    new_name = new_template.format(index)
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    shutil.move(old_path, new_path)
    print(f"Renamed '{old_name}' to '{new_name}'")

print("Program has run successfully.")