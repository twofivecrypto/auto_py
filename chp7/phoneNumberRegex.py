import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())#Phone number found: 415-555-4242

#mo in this case means 'Match objects'
#shorter program than 'isPhoneNumber.py' but does the same thing.