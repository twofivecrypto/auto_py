'''
    Say we want to rename every file in some folder and also every file in every subfolder of that folder. That is, we
want to walk through the directory tree, touching each file as we go.
    Writing a program to do this could get trick, but Python provides a function to handle this process for us.
    
    Let's write an example program that uses teh os.walk() on a directory tree.
'''

import os

output_file = 'auto_py_output.txt'  # Specify the output file name

with open(output_file, 'w') as file:  # Open the output file in write mode
    for folderName, subfolders, filenames in os.walk('D:\\auto_py'):
        file.write('The current folder is ' + folderName + '\n')
    
        for subfolder in subfolders:
            file.write('SUBFOLDER OF ' + folderName + ': ' + subfolder + '\n')
            
            for filename in filenames:
                file.write('FILE INSIDE ' + folderName + ': ' + filename + '\n')
        
        file.write('\n')
        
print(f"Output saved to: {output_file}")
