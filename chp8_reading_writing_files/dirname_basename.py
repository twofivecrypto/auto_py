import os

example = 'D:\\auto_py\chp8_reading_writing_files\dirname_basename.py' #DIR name is all folders(dirs), BASE name is .py or(.exe, .txt, etc etc) file

print(os.path.basename(example))#dirname_basename.py
print(os.path.dirname(example))#D:\auto_py\chp8_reading_writing_files

#use .split() to return a tuple value with two strings:
print('\n')
print(os.path.split(example))#('D:\\auto_py\\chp8_reading_writing_files', 'dirname_basename.py')

#USING os.sep to return a LIST
print(example.split(os.path.sep))#['D:', 'auto_py', 'chp8_reading_writing_files', 'dirname_basename.py']
