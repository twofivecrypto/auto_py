import shutil, os

#os.chdir('D:\\')

# Copy a specific file from the source path to the destination path
#shutil.copy2('D:\\auto_py\\ch1_basics\\index.html', 'D:\\auto_py\\chp9_organizing_files')

# Copy and rename a specific file from the source path to the destination path
#shutil.copy('D:\\auto_py\\chp9_organizing_files\\index.html', 'D:\\auto_py\\solo_p')

# moving and renaming files

#just move to new location (source, destination)
shutil.move('D:\\auto_py\\solo_p\\template.html', 'D:\\auto_py\\projects')
#move and rename
shutil.move('D:\\auto_py\\solo_p\\template.html', 'D:\\auto_py\\chp9_organizing_files\\template2.html')

