import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) #Batmobile
print(mo.group(1)) #mobile


print('\n--')

import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group()) #Batman
print(mo2.group()) #Batwoman

print('\n--')

import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo1.group()) #Batman
print(mo2.group()) #Batwoman
print(mo3.group()) #Batwowowowoman
mo3 = batRegex.search('The Adventures of Batman')
print('\v\f\n')
print(mo3.group())#Batman
print(mo3 == None)#False
print(mo3 != None)#True



