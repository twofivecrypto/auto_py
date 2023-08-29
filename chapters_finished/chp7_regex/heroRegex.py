import re

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')

print(mo1.group()) #Batman
print(mo2.group()) #Tina Fey

#we can also use the findall() method discussed in page 157



