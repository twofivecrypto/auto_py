import zipfile, os
os.chdir('D:\Web-Dev-For-Beginners-main.zip') #MOVE TO THE FOLDER WITH example.zip
exampleZip = zipFile.ZipFile('example.zip')
exampleZip.namelist()