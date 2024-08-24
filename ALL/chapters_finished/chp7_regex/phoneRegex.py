import re
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo2 = phoneRegex.search('My number is 555-4242')
print(mo1.group()) #415-555-4242
print(mo2.group()) #555-4242

