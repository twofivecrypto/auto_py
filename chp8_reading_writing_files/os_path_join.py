import os

print(os.path.join('usr', 'bin', 'spam'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\auto_py\\chp8_reading_writing_files', filename))