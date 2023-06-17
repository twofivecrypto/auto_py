import zipfile, os
#READING ZIP FILES
os.chdir('C:\\')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()

spamInfo = exampleZip.read('spam.txt').getinfo('spam.txt')
print(spamInfo.file_size)

spamInfo.compress_size

print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

#EXTRACTING FROM ZIP FILES
os.chdir('C:\\')
exampleZip = zipfile.ZipFile('example.zip') #move to the folder with example.zip
exampleZip.extractall()
exampleZip.close()

exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()

#CREATING AND ADDING TO ZIP FILES

#If you want to simply add files to an existing ZIP file, pass 'a' as a second argument to zipfile.ZipFile() to open the ZIP file in append mode. 
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


