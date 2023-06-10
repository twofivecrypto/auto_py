import shutil
import os

os.chdir('D:\\')

# Copy a specific file from the source path to the destination path
shutil.copy('D:\\ch1_basics\\filename.txt', 'D:\\chp7_regex\\')

# Copy and rename a specific file from the source path to the destination path
shutil.copy('D:\\letsGo.py', 'D:\\chp7_regex\\letsGo2.py')
