import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
print(mo1.group()) #HaHaHa
print(mo2 == None) #True

print('\n\v\n\f\n')

greedyHaRegex = re.compile(r'(Ha){3,5}')
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) #HaHaHaHaHa
print(mo2.group()) #HaHaHa

