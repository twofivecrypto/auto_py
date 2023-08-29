'''
myHeroes = ['Naruto', 'Goku', 'Sundiata', 'Mansa Musa']
print('Enter one of my heroes:')
name = input()
if name not in myHeroes:
    print("Wrong answer, " + name.title() + " isn't one of my childhood heroes.")
elif name == 'Sundiata':
    print(name + ' is the hero of my adult life.')
elif name == 'Mansa Musa':
    print(name + ' is a hero figure from my teenage years.')
elif name == 'Goku':
    print(name.title() + ', albeit fictional, is an anime character which greatly influenced my development.')
else:
    print(name.title() + ' is one of my childhood heroes, and one of the best.')

'''


print('\n--------\n')
print('The Multiple Assignment Trick')

print('\n\tThis is the regular way\n')
naruto = ['hokage', 'leaf', 'rasengan']
rank = naruto[0]
village = naruto[1]
jutsu = naruto[2]

#THE TRICK

naruto = ['hokage', 'leaf', 'rasengan']
rank, village, jutsu = naruto


#AUGMENTED ASSIGNMENT OPERATORS
spam = 42
spam = spam + 1
print(spam)
print('------')
#OR USE THE AUGMENTED OPERATOR
spam = 21
spam += 1
print(spam)

#CAN ALSO DO STRING CONCATENATION
spam = 'Hello'
spam += ' world'
print(spam)

spam *= 3
print(spam)