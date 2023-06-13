'''
Permanently deleting files and folders--

calling os.unlink(path) will delete the file at path
calling os.rmdir(path) will delete tehe folder at path, this folder MUST be COMPLETELY EMPTY
calling shutil.rmtree(path) will remove teh folder at path, and all files and folders will be deleted also

Good Practices:
Its a good idea to run program first with print() calls displaying which files will be deleted before uncommenting the deletions.

--

#A loop that deletes files that have the .txt file extension

import os
for filename in os.listdir():
    if filename.endswith('.txt'):
    #os.unlink(filename)
    print(filename)

'''


#SAFE DELETES WITH THE send2trash MODULE

import send2trash

#indexFile = open('newFile.txt', 'a')
#indexFile.write('The Mansaba has returned.')
#print('Proceed to delete file?? [enter any key to delete]')
#indexFile.close()
send2trash.send2trash('newFile.txt')