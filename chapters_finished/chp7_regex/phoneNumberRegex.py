import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())#Phone number found: 415-555-4242

#mo in this case means 'Match objects'
#shorter program than 'isPhoneNumber.py' but does the same thing.

#adding ( ) will create groups, lets say we wanted to isolate the area codes
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')

print(mo.group(1)) #415
print(mo.group(2)) #555
print(mo.group(0)) #415-555-4242
print(mo.group()) #415-555-4242
#retrive all the groups at once
print(mo.groups())#('415', '555', '4242')
print('\n')
areaCode, mainNumber = mo.groups()
print(areaCode) #415
print(mainNumber) #555-4242
#note if there were 3 groups of parenthesis, you'd need another variable besides 'areaCode' & 'mainNumber'.
#if the number has a parenthesis in it already, you need the escape the ( and ) characters with a backslash

import re

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415)-555-4242.')

print(mo.group(1))  # (415)
print(mo.group(2))  # 555-4242






