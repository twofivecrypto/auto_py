import traceback
#import os

try:
    raise Exception('This is the error message.')
except:
    #Specify the file path
    #file_path = os.path.join(r'D:\\auto_py\\chp10_debuggin', 'errorInfo.txt')
    
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')