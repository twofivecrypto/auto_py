import zipfile
import os

# Set the working directory to the folder containing the ZIP file
os.chdir('D:\\')

# Specify the path to the ZIP file
zip_path = 'D:\Automate_the_Boring_Stuff_onlinematerials_v.2.zip'

# Extract the folder name from the ZIP file path
zip_folder_name = os.path.splitext(os.path.basename(zip_path))[0]

# Open the ZIP file
exampleZip = zipfile.ZipFile(zip_path)

# List the files in the ZIP archive
file_list = exampleZip.namelist()

# Save the file list to a text file named after the zip folder
output_file = f'{zip_folder_name}_file_list.txt'

# Open the output file in write mode
with open(output_file, 'w') as f:
    for file_path in file_list:
        # Create the directory structure if it doesn't exist
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        # Write the file path to the output file
        f.write(file_path + '\n')

# Close the ZIP file
exampleZip.close()

# Print the path to the output file
print('File list saved to', output_file)
