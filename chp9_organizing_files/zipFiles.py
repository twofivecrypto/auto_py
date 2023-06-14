import zipfile, os

# Set the working directory to the folder containing the ZIP file
os.chdir('D:\\')


# Specify the path to the ZIP file
zip_path = 'D:\\Web-Dev-For-Beginners-main.zip'

#Open the ZIP file
exampleZip = zipfile.ZipFile(zip_path)

#List the files in the zip archive
file_list = exampleZip.namelist()
#print(file_list)
fileInfo = exampleZip.getinfo('README.el.md')
print(fileInfo.file_size)