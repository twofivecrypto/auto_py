#FOR LOOPS ALWAYS INCLUDE THE FOLLOWING:
'''
1 - THE for KEYWORD
2 - A VARIABLE NAME
3 - THE in KEYWORD
4 - A CALL TO THE range() METHOD WITH UP TO 3 INTEGERS PASSED TO IT
5 - A COLON
6 - AN INDENTION ON NEXT LINE, BLOCK OF CODE (CALLED THE for clause)
'''


'''
print('My name is')
for i in range(5):
    print('Famara Five Times (' + str(i) + ')')


print('\n\n')

total = 0
for num in range(101):
    total = total + num
print(total)

'''

print('\n\n')

print('My name is')
i = 0
while i < 5:
    print('The Return of the Mansaba (' + str(i) + ')')
    i = i + 1


print('\n')

#STARTING AND STOPPING ARGUMENTS TO range()
for i in range(12, 16):
    print(i)

line_space = print('\n---------\n')

#STEPPING ARGUMENTS TO range()
for i in range(0, 50, 10):
    print(i)

print('\n---------\n')

#COUNTING DOWN
for i in range(5, -1, -1):
    print(i)

print('\n---------\n')