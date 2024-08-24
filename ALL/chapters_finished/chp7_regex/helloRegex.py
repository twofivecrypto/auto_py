import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!')) # <sre.SRE_Match object; span=(0,5), match='Hello'>
print(beginsWithHello.search('He said hello')) # None
print('\n----\n')
endsWithNumber = re.compile(r'\d$')#matches strings that end with a numeric character from 0 - 9.
print(endsWithNumber.search('Your number is 42')) #<re.Match object; span=(16, 17), match='2'>
print(endsWithNumber.search('Your number is forty two.') == None) #True
print('\n----\n')
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))#<re.Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890') == None)#True
print(wholeStringIsNum.search('12   34567890') == None)#True


