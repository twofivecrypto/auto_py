import re

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maides, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maides', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
print('\n\v\f\n')

print('Making Your Own Classes\n----------\n')

vowelRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex = re.compile(r'[^aeiouAEIOU]')

print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
print('\n----')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.')) #['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

