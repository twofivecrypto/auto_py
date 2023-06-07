import os

#os.makedirs('D:\\leetCodeLearner\\GPT\\Tutorials')

#HANDLING ABSOLUTE & RELATIVE PATHS

print(os.path.abspath('.'))#D:\auto_py
print(os.path.abspath('.\\Scripts'))#D:\auto_py\Scripts
print(os.path.isabs('.'))#False
print(os.path.isabs(os.path.abspath('.')))#True

print(os.path.relpath('D:\\auto_py', 'D:\\'))#autopy
print(os.path.relpath('D:\\auto_py', 'D:\\projects\\Password Locker'))#..\..\auto_py
print(os.getcwd())#D:\auto_py


