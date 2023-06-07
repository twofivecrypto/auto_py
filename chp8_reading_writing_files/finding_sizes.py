import os

# Get the size of the file and print it in bytes
file_size = os.path.getsize('D:\\auto_py\\chp8_reading_writing_files\\dirname_basename.py')
print(f"File Size: {file_size} bytes")

# List the files in the directory
print(os.listdir('C:\\Users\\94M0\\Documents\\PYTHON'))

print('\n----')

total_size = 0

# Iterate over the files in the directory
for filename in os.listdir('C:\\Users\\94M0\\Documents\\PYTHON'):
    # Get the size of each file and add it to the total size
    total_size += os.path.getsize(os.path.join('C:\\Users\\94M0\\Documents\\PYTHON', filename))

# Convert the total size to megabytes
file_size_mb = total_size / (1024 * 1024)

print(total_size)  # Print the total size in bytes
print(str(file_size_mb) + ' MB')  # Print the total size in megabytes
'''
Output
*32768
*0.03125 MB
'''