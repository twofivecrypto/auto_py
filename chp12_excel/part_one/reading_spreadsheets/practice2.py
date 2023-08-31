import os
os.chdir('D:\\auto_py')
import census2010
census2010.allData['AK']['Anchorage']
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))