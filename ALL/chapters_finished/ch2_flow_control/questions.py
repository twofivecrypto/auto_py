'''



'''
spam = 0
spam = spam + 1
while spam == 1:
    print('Hello')
    if spam == 2:
        print('Howdy')
    else:
        print('Greetings, partner')
        break

print("\n\n")

for i in range(0, 1000, 100):
    print(i)
print('\n')
for i in range(5):
    print(i)
print('\n')

for i in range(10):
    print(i)

'''while i in range(10):
    print(i)
'''

#Mansa 10x w a counter
for i in range(1, 11):
    print(str(int(i)) + ' - Mansa')

for i in range(0,3):
    print(i)

#USING A WHILE LOOP
i = 1
while i <= 10:
    print(str(int(i)) + ' - Returns')
    i += 1

i = 2
while i <= 4:
    print(i)
    i += 1

'''
HOW TO CALL FUNCTION bacon() FROM MODULE spam AFTER IMPORTING SPAM?

import spam

spam.bacon()
'''
#round() FUNCTION ROUNDS NUMBERS TO SPECIFIC DECIMAL PLACE
print('\n--------\n')
number = 4.6
rounded_number = round(number)
print(rounded_number)

print('\n--------\n')

#abs() COUNTS DISTANCE BETWEEN TWO POINTS, + OR -
numeral = -11
absolute_value = abs(numeral)
print(absolute_value)

print('\nTOTAL\n')

print(rounded_number + absolute_value)